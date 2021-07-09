from flask import Flask, render_template, request
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="j5xyhrmpft4yjspy",
        public_key="67kcssmkb84nxjsh",
        private_key="51b70b4accd78bb7fdec8baaa0f9b704"
    )
)
app = Flask(__name__)

@app.route('/')
def home():
    # pass client_token to your front-end
    token = gateway.client_token.generate()
    print(token)
    return render_template('home.html', token = token)

@app.route('/', methods=['POST'])
def payment():
    nonce = request.form['nonce']
    gateway.transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": nonce,
    "options": {
      "submit_for_settlement": True
    }
})
    return '12312321321'