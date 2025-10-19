---
name: rainforest-integration
description: Implement RainforestPay embedded payment processing for vertical SaaS platforms with secure components, API integration, and webhook handling. Use when building embedded payments for SaaS platforms, reducing PCI scope, or implementing white-label payment solutions.
---

# RainforestPay Integration

Master RainforestPay embedded payment processing for vertical SaaS platforms with secure payment components, API integration, and PCI-compliant payment flows.

## When to Use This Skill

- Building embedded payments for vertical SaaS platforms
- Implementing white-label payment solutions for merchants
- Reducing PCI compliance scope with embedded components
- Processing payments on behalf of merchants (platform model)
- Implementing payment flows that need to be merchant-branded
- Building marketplace or platform payment infrastructure
- Migrating from general-purpose payment processors to embedded payments

## Why RainforestPay vs. Stripe/Other Processors

**RainforestPay specializes in:**
- **Embedded payments for SaaS platforms**: Built specifically for platforms that facilitate payments for their merchants
- **Reduced PCI scope**: Payment components that collect sensitive data without exposing your platform
- **Merchant management**: Built-in tools for managing multiple merchants and their payment configurations
- **Platform economics**: Revenue sharing and fee management for platform business models

**Use RainforestPay when:**
- You're a vertical SaaS platform facilitating payments for your customers
- You need to reduce PCI compliance burden significantly
- You want embedded, white-label payment experiences
- You have a platform or marketplace business model

**Use Stripe/Others when:**
- You're processing payments for your own business (not on behalf of merchants)
- You need broader global payment method coverage
- You need extensive ecosystem integrations

## Core Concepts

### 1. Integration Approaches

**Component-Based Integration (Recommended)**
- Embeddable payment UI components
- Sensitive data collected directly by Rainforest
- Minimal PCI compliance scope
- Customizable styling
- Fastest implementation

**API-Only Integration**
- Complete UI control
- Direct API integration
- Higher PCI compliance requirements
- Maximum customization

**Hybrid Approach**
- Mix components for sensitive data collection
- API for custom workflows
- Balance of compliance and customization

### 2. Key Objects

**Payin Config**
- Pre-payment setup with amount, currency, metadata
- Like Stripe's Payment Intent
- Created before collecting payment details

**Session**
- Grants permissions to payment components
- Controls what actions components can perform
- Time-limited authorization token

**Payin**
- Actual payment transaction
- Created by component or API
- Contains payment method and processing status

**Merchant**
- Business entity receiving payments
- Managed by your platform
- Has own payment configuration

### 3. Payment Flow

1. **Create Payin Config** → Set amount, currency, merchant
2. **Create Session** → Grant component permissions
3. **Render Component** → Collect payment details securely
4. **Process Payin** → Component creates and processes payment
5. **Webhook Notification** → Receive payment status updates

### 4. API Versioning

**Current Recommended Version**: `2023-12-01`
**Deprecated Version**: `2023-01-01` (end of life: May 1, 2025)

Always specify API version in headers:
```
Rainforest-API-Version: 2023-12-01
```

## Quick Start

### Installation

```bash
# Python
pip install rainforest-pay

# Node.js
npm install @rainforestpay/rainforest-js

# Ruby
gem install rainforest
```

### Basic Setup

```python
import rainforest

# Configure API key
rainforest.api_key = 'sk_live_...'
rainforest.api_version = '2023-12-01'
```

```javascript
// Node.js
const Rainforest = require('@rainforestpay/rainforest-js');
const rainforest = new Rainforest('sk_live_...', {
  apiVersion: '2023-12-01'
});
```

### Create Payment with Component (Recommended)

```python
# Backend: Create payin config and session
def create_payment_session(amount, currency='USD', merchant_id=None):
    """Create a payin config and session for component-based payment."""

    # Step 1: Create payin config
    payin_config = rainforest.PayinConfig.create(
        amount=amount * 100,  # Amount in cents
        currency=currency,
        merchant=merchant_id,
        metadata={
            'order_id': 'order_123',
            'customer_id': 'customer_456'
        }
    )

    # Step 2: Create session with permissions
    session = rainforest.Session.create(
        permissions=[
            'payin:create',
            'payin_config:read'
        ],
        resources={
            'payin_configs': [payin_config.id]
        }
    )

    return {
        'payin_config_id': payin_config.id,
        'session_key': session.key
    }
```

```javascript
// Frontend: Render payment component
import { RainforestPaymentComponent } from '@rainforestpay/components';

function CheckoutPage() {
  const [sessionData, setSessionData] = useState(null);

  useEffect(() => {
    // Fetch session from your backend
    fetch('/api/create-payment-session', {
      method: 'POST',
      body: JSON.stringify({ amount: 50.00, currency: 'USD' })
    })
      .then(res => res.json())
      .then(data => setSessionData(data));
  }, []);

  if (!sessionData) return <div>Loading...</div>;

  return (
    <RainforestPaymentComponent
      sessionKey={sessionData.session_key}
      payinConfigId={sessionData.payin_config_id}
      onSuccess={(payin) => {
        console.log('Payment successful:', payin.id);
        // Redirect to success page
      }}
      onError={(error) => {
        console.error('Payment failed:', error);
        // Show error to user
      }}
      style={{
        primaryColor: '#007bff',
        borderRadius: '8px'
      }}
    />
  );
}
```

## Integration Patterns

### Pattern 1: Component-Based Payment (PCI-Friendly)

```python
# Backend API endpoint
from flask import Flask, request, jsonify
import rainforest

app = Flask(__name__)
rainforest.api_key = 'sk_live_...'
rainforest.api_version = '2023-12-01'

@app.route('/api/create-payment', methods=['POST'])
def create_payment():
    """Create payin config and session for component."""
    data = request.json
    amount = data['amount']
    merchant_id = data['merchant_id']

    try:
        # Create payin config
        payin_config = rainforest.PayinConfig.create(
            amount=int(amount * 100),  # Convert to cents
            currency=data.get('currency', 'USD'),
            merchant=merchant_id,
            description=data.get('description', ''),
            metadata={
                'order_id': data.get('order_id'),
                'customer_email': data.get('customer_email')
            },
            # Optional: Add customer info
            billing_details={
                'name': data.get('customer_name'),
                'email': data.get('customer_email'),
                'address': data.get('billing_address')
            }
        )

        # Create session for component
        session = rainforest.Session.create(
            permissions=['payin:create', 'payin_config:read'],
            resources={
                'payin_configs': [payin_config.id]
            },
            # Session expires in 1 hour
            expires_at=int(time.time()) + 3600
        )

        return jsonify({
            'success': True,
            'payin_config_id': payin_config.id,
            'session_key': session.key
        })

    except rainforest.error.RainforestError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
```

```html
<!-- Frontend: Payment component integration -->
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.rainforestpay.com/v2/components.js"></script>
</head>
<body>
    <div id="payment-component"></div>

    <script>
        async function initializePayment() {
            // Fetch session from backend
            const response = await fetch('/api/create-payment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    amount: 99.99,
                    merchant_id: 'merchant_123',
                    order_id: 'order_456',
                    customer_email: 'customer@example.com',
                    customer_name: 'John Doe'
                })
            });

            const data = await response.json();

            if (!data.success) {
                console.error('Failed to create payment:', data.error);
                return;
            }

            // Initialize Rainforest component
            const rainforest = Rainforest(data.session_key);

            // Create and mount payment component
            const paymentComponent = rainforest.createPaymentComponent({
                payinConfigId: data.payin_config_id,
                style: {
                    base: {
                        color: '#32325d',
                        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
                        fontSize: '16px',
                    },
                    invalid: {
                        color: '#fa755a',
                    }
                }
            });

            paymentComponent.mount('#payment-component');

            // Handle payment submission
            paymentComponent.on('submit', async (event) => {
                const { payin, error } = await paymentComponent.processPayment();

                if (error) {
                    console.error('Payment error:', error);
                    showError(error.message);
                } else {
                    console.log('Payment successful:', payin.id);
                    window.location.href = '/success?payin_id=' + payin.id;
                }
            });
        }

        initializePayment();
    </script>
</body>
</html>
```

### Pattern 2: API-Only Payment Flow

```python
def process_payment_api_only(amount, currency, payment_method_token, merchant_id):
    """Process payment entirely via API (requires PCI compliance)."""

    try:
        # Create and process payin in one step
        payin = rainforest.Payin.create(
            amount=int(amount * 100),
            currency=currency,
            merchant=merchant_id,
            payment_method=payment_method_token,  # From frontend tokenization
            capture=True,  # Capture immediately
            metadata={
                'integration_type': 'api_only'
            }
        )

        # Check payment status
        if payin.status == 'succeeded':
            return {
                'success': True,
                'payin_id': payin.id,
                'amount': payin.amount,
                'status': payin.status
            }
        else:
            return {
                'success': False,
                'error': f'Payment status: {payin.status}',
                'payin_id': payin.id
            }

    except rainforest.error.CardError as e:
        # Card was declined
        return {
            'success': False,
            'error': e.user_message,
            'decline_code': e.decline_code
        }
    except rainforest.error.RainforestError as e:
        # Other Rainforest errors
        return {
            'success': False,
            'error': str(e)
        }
```

### Pattern 3: Merchant Onboarding

```python
def onboard_merchant(business_info):
    """Onboard a new merchant to your platform."""

    merchant = rainforest.Merchant.create(
        business_name=business_info['business_name'],
        business_type=business_info['business_type'],  # 'individual', 'company'
        email=business_info['email'],

        # Business details
        business_info={
            'tax_id': business_info.get('tax_id'),
            'address': {
                'line1': business_info['address_line1'],
                'line2': business_info.get('address_line2'),
                'city': business_info['city'],
                'state': business_info['state'],
                'postal_code': business_info['postal_code'],
                'country': business_info['country']
            }
        },

        # Bank account for payouts
        bank_account={
            'account_number': business_info['account_number'],
            'routing_number': business_info['routing_number'],
            'account_holder_name': business_info['account_holder_name']
        },

        # Platform settings
        metadata={
            'platform_merchant_id': business_info.get('internal_id'),
            'onboarding_date': str(datetime.now())
        }
    )

    return merchant
```

### Pattern 4: Multi-Merchant Payment Splitting

```python
def create_split_payment(total_amount, merchant_splits):
    """
    Create a payment that splits funds between multiple merchants.

    Args:
        total_amount: Total payment amount
        merchant_splits: List of {'merchant_id': str, 'amount': float, 'description': str}
    """

    payins = []

    for split in merchant_splits:
        payin_config = rainforest.PayinConfig.create(
            amount=int(split['amount'] * 100),
            currency='USD',
            merchant=split['merchant_id'],
            description=split.get('description', ''),
            metadata={
                'split_payment': True,
                'total_amount': total_amount
            }
        )

        payins.append({
            'merchant_id': split['merchant_id'],
            'amount': split['amount'],
            'payin_config_id': payin_config.id
        })

    return payins
```

## Webhook Handling

### Secure Webhook Endpoint

```python
from flask import Flask, request, abort
import rainforest
import hmac
import hashlib

app = Flask(__name__)

WEBHOOK_SECRET = 'whsec_...'  # From Rainforest dashboard

@app.route('/webhooks/rainforest', methods=['POST'])
def rainforest_webhook():
    """Handle Rainforest webhook events."""

    payload = request.data
    signature = request.headers.get('Rainforest-Signature')

    # Verify webhook signature
    if not verify_webhook_signature(payload, signature, WEBHOOK_SECRET):
        abort(401)

    event = request.json
    event_type = event['type']
    event_data = event['data']

    # Handle different event types
    if event_type == 'payin.succeeded':
        handle_payin_succeeded(event_data)
    elif event_type == 'payin.failed':
        handle_payin_failed(event_data)
    elif event_type == 'payin.refunded':
        handle_payin_refunded(event_data)
    elif event_type == 'merchant.updated':
        handle_merchant_updated(event_data)
    elif event_type == 'payout.paid':
        handle_payout_paid(event_data)
    else:
        print(f'Unhandled event type: {event_type}')

    return 'OK', 200

def verify_webhook_signature(payload, signature, secret):
    """Verify Rainforest webhook signature."""
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(signature, f'sha256={expected_signature}')

def handle_payin_succeeded(payin_data):
    """Process successful payment."""
    payin_id = payin_data['id']
    amount = payin_data['amount']
    merchant_id = payin_data['merchant']
    metadata = payin_data.get('metadata', {})

    # Update database
    # Fulfill order
    # Send confirmation email

    print(f'Payment succeeded: {payin_id}, Amount: ${amount/100:.2f}')

def handle_payin_failed(payin_data):
    """Handle failed payment."""
    payin_id = payin_data['id']
    error = payin_data.get('error', {})

    # Update order status
    # Notify customer of failure
    # Log for analytics

    print(f'Payment failed: {payin_id}, Error: {error.get("message")}')

def handle_payin_refunded(payin_data):
    """Handle payment refund."""
    payin_id = payin_data['id']
    refund_amount = payin_data.get('refund_amount')

    # Update database
    # Process refund in internal systems
    # Send refund confirmation email

    print(f'Payment refunded: {payin_id}, Amount: ${refund_amount/100:.2f}')

def handle_merchant_updated(merchant_data):
    """Handle merchant updates."""
    merchant_id = merchant_data['id']

    # Sync merchant data
    # Update merchant settings

    print(f'Merchant updated: {merchant_id}')

def handle_payout_paid(payout_data):
    """Handle payout completion."""
    payout_id = payout_data['id']
    merchant_id = payout_data['merchant']
    amount = payout_data['amount']

    # Update payout records
    # Notify merchant

    print(f'Payout completed: {payout_id}, Merchant: {merchant_id}')
```

### Webhook Event Types

**Payment Events:**
- `payin.created`: Payment created
- `payin.succeeded`: Payment successful
- `payin.failed`: Payment failed
- `payin.refunded`: Refund processed
- `payin.disputed`: Chargeback initiated

**Merchant Events:**
- `merchant.created`: New merchant onboarded
- `merchant.updated`: Merchant details changed
- `merchant.verification.completed`: Merchant verified
- `merchant.verification.failed`: Merchant verification failed

**Payout Events:**
- `payout.created`: Payout initiated
- `payout.paid`: Payout completed
- `payout.failed`: Payout failed

## Refunds and Disputes

### Create Refund

```python
def create_refund(payin_id, amount=None, reason=None):
    """
    Refund a payment.

    Args:
        payin_id: ID of the payin to refund
        amount: Amount to refund (None for full refund)
        reason: Reason for refund
    """

    refund_params = {
        'payin': payin_id
    }

    if amount:
        refund_params['amount'] = int(amount * 100)  # Partial refund

    if reason:
        refund_params['reason'] = reason

    refund = rainforest.Refund.create(**refund_params)

    return {
        'refund_id': refund.id,
        'amount': refund.amount,
        'status': refund.status
    }
```

### Handle Dispute

```python
def respond_to_dispute(dispute_id, evidence):
    """Submit evidence for a payment dispute."""

    rainforest.Dispute.update(
        dispute_id,
        evidence={
            'customer_name': evidence.get('customer_name'),
            'customer_email': evidence.get('customer_email'),
            'shipping_tracking_number': evidence.get('tracking_number'),
            'customer_communication': evidence.get('communication'),
            'receipt': evidence.get('receipt_url')
        }
    )
```

## Testing

### Test Mode

```python
# Use test API key
rainforest.api_key = 'sk_test_...'

# Test card numbers
TEST_CARDS = {
    'success': '4242424242424242',
    'decline_insufficient_funds': '4000000000009995',
    'decline_lost_card': '4000000000009987',
    'decline_stolen_card': '4000000000009979',
    'require_3ds': '4000002500003155'
}
```

### Component Studio

RainforestPay provides a Component Studio at `docs.rainforestpay.com/component-studio` for:
- Visual component customization
- Style configuration
- Live preview
- Code generation

### Sandbox Testing

```python
def test_payment_flow():
    """Test complete payment flow in sandbox."""

    # Create test merchant
    merchant = rainforest.Merchant.create(
        business_name='Test Business',
        business_type='individual',
        email='test@example.com'
    )

    # Create payin config
    payin_config = rainforest.PayinConfig.create(
        amount=5000,  # $50.00
        currency='USD',
        merchant=merchant.id
    )

    # Create session
    session = rainforest.Session.create(
        permissions=['payin:create', 'payin_config:read'],
        resources={'payin_configs': [payin_config.id]}
    )

    # In real scenario, session_key would be used in frontend
    assert session.key is not None
    assert payin_config.id is not None
```

## Migration from API v2023-01-01 to v2023-12-01

### Key Changes

1. **Simplified Authorization**: Sessions replace complex permission models
2. **Payin Config**: New object for pre-payment setup
3. **Component Improvements**: Better customization and error handling

### Migration Steps

```python
# Old API (2023-01-01)
rainforest.api_version = '2023-01-01'
payment = rainforest.Payment.create(
    amount=1000,
    currency='USD'
)

# New API (2023-12-01)
rainforest.api_version = '2023-12-01'

# Step 1: Create payin config
payin_config = rainforest.PayinConfig.create(
    amount=1000,
    currency='USD'
)

# Step 2: Create session
session = rainforest.Session.create(
    permissions=['payin:create'],
    resources={'payin_configs': [payin_config.id]}
)

# Step 3: Use in component or API
```

## PCI Compliance

### Component-Based Integration (SAQ A)

When using Rainforest payment components:
- **PCI Level**: SAQ A (simplest)
- **Requirements**: Annual questionnaire + network scan
- **Scope**: Minimal (Rainforest handles card data)

**Implementation:**
```python
# Payment data never touches your server
# Component sends directly to Rainforest
session = create_payment_session(amount=100.00)
# Return session_key to frontend component
```

### API-Only Integration (SAQ D)

When handling card data via API:
- **PCI Level**: SAQ D (most complex)
- **Requirements**: Full PCI DSS compliance audit
- **Scope**: Extensive

**Recommendation**: Use component-based integration unless you have specific UI requirements that cannot be met with component customization.

## Best Practices

### 1. Always Use Components When Possible
Minimize PCI compliance scope by using Rainforest payment components for sensitive data collection.

### 2. Implement Webhook Idempotency
```python
def process_webhook_event(event_id, handler):
    """Ensure webhook events are processed exactly once."""
    if event_already_processed(event_id):
        return

    try:
        handler()
        mark_event_processed(event_id)
    except Exception as e:
        log_error(e)
        raise  # Rainforest will retry
```

### 3. Secure Your Webhooks
- Always verify webhook signatures
- Use HTTPS endpoints
- Implement rate limiting
- Log all webhook events

### 4. Handle Merchant Lifecycle
```python
def manage_merchant_status(merchant_id):
    """Monitor and manage merchant verification status."""
    merchant = rainforest.Merchant.retrieve(merchant_id)

    if merchant.verification_status == 'pending':
        # Notify merchant of pending verification
        pass
    elif merchant.verification_status == 'verified':
        # Enable payment processing
        pass
    elif merchant.verification_status == 'failed':
        # Request additional information
        pass
```

### 5. Use Metadata Extensively
Link Rainforest objects to your database:
```python
payin_config = rainforest.PayinConfig.create(
    amount=5000,
    currency='USD',
    metadata={
        'order_id': 'ord_123',
        'customer_id': 'cus_456',
        'product_sku': 'PROD-789',
        'campaign': 'summer-sale'
    }
)
```

### 6. Monitor API Version Deprecations
- Subscribe to Rainforest API announcements
- Test new API versions in sandbox
- Plan migrations well before deprecation dates
- Use API versioning headers consistently

### 7. Implement Proper Error Handling
```python
try:
    payin = rainforest.Payin.create(...)
except rainforest.error.CardError as e:
    # Card declined - show user-friendly message
    print(f"Card declined: {e.user_message}")
except rainforest.error.InvalidRequestError as e:
    # Invalid parameters - fix the request
    print(f"Invalid request: {e}")
except rainforest.error.AuthenticationError as e:
    # Authentication failed - check API keys
    print(f"Authentication error: {e}")
except rainforest.error.APIConnectionError as e:
    # Network error - retry
    print(f"Network error: {e}")
except rainforest.error.RainforestError as e:
    # Generic error
    print(f"Rainforest error: {e}")
```

## Resources

- **references/component-integration.md**: Detailed component setup and customization
- **references/api-migration-guide.md**: Migration from v2023-01-01 to v2023-12-01
- **references/merchant-onboarding.md**: Complete merchant onboarding flow
- **references/webhook-events.md**: All webhook events and payloads
- **references/pci-compliance.md**: PCI compliance guidance
- **assets/rainforest-client.py**: Production-ready Python client wrapper
- **assets/webhook-handler.py**: Complete webhook processor with signature verification
- **assets/payment-component.html**: Frontend component integration examples

## Common Pitfalls

- **Not Verifying Webhooks**: Always verify webhook signatures to prevent spoofing
- **Missing API Version Header**: Always specify `Rainforest-API-Version` header
- **Storing Card Data**: Never log or store raw card numbers (violates PCI)
- **Ignoring Webhook Failures**: Implement retry logic and monitoring
- **Hardcoding Merchant IDs**: Use dynamic merchant lookup based on context
- **Incomplete Error Handling**: Handle all Rainforest error types gracefully
- **Not Testing in Sandbox**: Always test payment flows in sandbox before production
- **Forgetting Refund Windows**: Process refunds within allowed timeframes

## Support and Documentation

- **Official Docs**: https://docs.rainforestpay.com
- **Component Studio**: https://docs.rainforestpay.com/component-studio
- **API Reference**: https://docs.rainforestpay.com/v2023-12-01/docs
- **Developer Slack**: Partner with senior integration engineers
- **API Logs**: Real-time logs in Rainforest dashboard
