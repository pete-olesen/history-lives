"""
Shared authentication and usage tracking for History Lives.

Usage is tracked in a simple JSON file (usage_log.json) keyed by access code.
Each code has a message limit. Once exhausted, the user sees a friendly message.

This is intentionally simple - good enough to prevent casual abuse of API credits
without the overhead of a real database or user accounts.
"""

import streamlit as st
import json
import os
from datetime import datetime

USAGE_FILE = os.path.join(os.path.dirname(__file__), "usage_log.json")


def get_valid_codes():
    """Returns dict of {code: message_limit} from secrets."""
    try:
        codes_raw = st.secrets["ACCESS_CODES"]
        # Format in secrets: "CODE1:50,CODE2:50,WIFE:200"
        codes = {}
        for pair in codes_raw.split(","):
            code, limit = pair.strip().split(":")
            codes[code.strip().upper()] = int(limit.strip())
        return codes
    except Exception:
        # Fallback for local testing without secrets configured
        return {"DEMO": 50, "TEACHER": 100}


def load_usage():
    """Load usage log from disk."""
    if os.path.exists(USAGE_FILE):
        try:
            with open(USAGE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_usage(usage):
    """Save usage log to disk."""
    try:
        with open(USAGE_FILE, "w") as f:
            json.dump(usage, f, indent=2)
    except Exception:
        pass  # Fail silently - don't break the app if disk write fails


def check_login():
    """
    Renders a login gate. Returns True if user is authenticated
    and has remaining usage. Sets st.session_state.access_code
    and st.session_state.messages_remaining on success.
    """
    if "access_code" in st.session_state:
        return True

    st.markdown("## History Lives")
    st.markdown("##### Enter your access code to begin")

    code_input = st.text_input("Access Code", placeholder="Enter code...", type="password")
    submitted = st.button("Enter")

    if submitted:
        valid_codes = get_valid_codes()
        code_upper = code_input.strip().upper()

        if code_upper in valid_codes:
            usage = load_usage()
            limit = valid_codes[code_upper]
            used = usage.get(code_upper, {}).get("count", 0)

            if used >= limit:
                st.error(
                    f"This access code has reached its usage limit ({limit} messages). "
                    "Please contact us for a new code."
                )
                return False

            st.session_state.access_code = code_upper
            st.session_state.message_limit = limit
            st.session_state.messages_used = used
            st.rerun()
        else:
            st.error("Invalid access code. Please check and try again.")

    st.markdown("---")
    st.caption(
        "Don't have a code? This is a research prototype for educators. "
        "Contact us to request access."
    )
    return False


def increment_usage():
    """Call this after each AI response to track usage."""
    code = st.session_state.get("access_code")
    if not code:
        return

    usage = load_usage()
    if code not in usage:
        usage[code] = {"count": 0, "first_used": datetime.now().isoformat()}

    usage[code]["count"] += 1
    usage[code]["last_used"] = datetime.now().isoformat()
    save_usage(usage)

    st.session_state.messages_used = usage[code]["count"]


def get_remaining_messages():
    """Returns (used, limit) tuple for the current session."""
    used = st.session_state.get("messages_used", 0)
    limit = st.session_state.get("message_limit", 0)
    return used, limit


def usage_sidebar():
    """Renders usage info in the sidebar."""
    used, limit = get_remaining_messages()
    remaining = max(0, limit - used)

    with st.sidebar:
        st.markdown("---")
        st.caption(f"**Access code:** {st.session_state.get('access_code', '')}")
        st.caption(f"**Messages remaining:** {remaining} / {limit}")
        if remaining <= 5 and remaining > 0:
            st.warning(f"Only {remaining} messages remaining on this code.")
        st.markdown("---")
        st.markdown(
            "📝 **[Share your feedback](https://forms.gle/Na4JCYTzWi5Yej727)**"
        )
        st.caption("3 minutes — your honest reaction shapes what gets built next.")
        if st.button("Log out"):
            for key in ["access_code", "message_limit", "messages_used"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()


def has_messages_remaining():
    """Check if the current code has messages left."""
    used, limit = get_remaining_messages()
    if used >= limit:
        st.error(
            "You've used all your messages for this access code. "
            "Thank you for trying History Lives! "
            "Please contact us if you'd like to continue exploring."
        )
        return False
    return True
