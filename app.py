import streamlit as st
import streamlit.components.v1 as components
import requests

# Pi Network Authentication Component
def pi_auth_component():
    return components.html(
        """
        <script src="https://sdk.minepi.com/pi-sdk.js"></script>
        <script>
            const Pi = window.Pi;
            Pi.init({ version: "2.0", sandbox: true });

            async function authenticate() {
                try {
                    await Pi.init();
                    const auth = await Pi.authenticate(["username"], onIncompletePaymentFound);
                    window.parent.postMessage({
                        type: 'pi_auth_success',
                        token: auth.accessToken,
                        user: auth.user.username
                    }, '*');
                } catch (err) {
                    window.parent.postMessage({ type: 'pi_auth_error', error: err }, '*');
                }
            }

            function onIncompletePaymentFound(payment) {
                console.log("Incomplete payment found", payment);
            }

            // Auto-trigger on load
            authenticate();
            
            // Expose for manual button
            window.manualAuth = authenticate;
        </script>
        """,
        height=0,
    )

# Backend Token Validation
def validate_pi_token(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.minepi.com/v2/me", headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# App Logic
st.title("Shahryar System")
pi_auth_component()

# Handle JS communication
if 'pi_user' not in st.session_state:
    st.session_state.pi_user = None

# Manual Sign-in Button
if st.button("Sign in with Pi"):
    components.html("<script>window.manualAuth();</script>", height=0)

# JS Response Listener
response = st.experimental_get_query_params() # Simplified for structure
# In a full deployment, use streamlit-javascript or custom component 
# to capture the postMessage event from the JS component.

if st.session_state.pi_user:
    st.write(f"Welcome, {st.session_state.pi_user}")
else:
    st.warning("Please authenticate with Pi to continue."
