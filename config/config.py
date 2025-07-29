import os
from dotenv import load_dotenv

load_dotenv()

# Product Configuration Options
PRODUCT_CONFIGS = {
    # Configuration 1: 30-Day Money-Back Guarantee (Recommended for SaaS)
    'money_back_30': {
        'name': 'YouGen: AI YouTube Content Generator',
        'price': '29.00',
        'currency': 'USD',
        'availability': 'https://schema.org/InStock',
        'return_policy': {
            'has_return_policy': True,
            'return_days': 30,
            'return_method': 'https://schema.org/ReturnByMail',
            'return_fees': 'https://schema.org/FreeReturn',
            'applicable_country': 'US'
        },
        'shipping': {
            'is_digital': True,
            'shipping_rate': '0',
            'handling_time': 0,
            'transit_time': 0,
            'shipping_country': 'US'
        }
    },
    
    # Configuration 2: 7-Day Money-Back Guarantee
    'money_back_7': {
        'name': 'YouGen: AI YouTube Content Generator',
        'price': '29.00',
        'currency': 'USD',
        'availability': 'https://schema.org/InStock',
        'return_policy': {
            'has_return_policy': True,
            'return_days': 7,
            'return_method': 'https://schema.org/ReturnByMail',
            'return_fees': 'https://schema.org/FreeReturn',
            'applicable_country': 'US'
        },
        'shipping': {
            'is_digital': True,
            'shipping_rate': '0',
            'handling_time': 0,
            'transit_time': 0,
            'shipping_country': 'US'
        }
    },
    
    # Configuration 3: No Return Policy (Digital Product)
    'no_returns': {
        'name': 'YouGen: AI YouTube Content Generator',
        'price': '29.00',
        'currency': 'USD',
        'availability': 'https://schema.org/InStock',
        'return_policy': {
            'has_return_policy': False,
            'return_days': 0,
            'return_method': None,
            'return_fees': None,
            'applicable_country': 'US'
        },
        'shipping': {
            'is_digital': True,
            'shipping_rate': '0',
            'handling_time': 0,
            'transit_time': 0,
            'shipping_country': 'US'
        }
    }
}

# Get configuration based on environment variable
def get_product_config():
    config_type = os.environ.get('RETURN_POLICY_TYPE', 'money_back_30')
    return PRODUCT_CONFIGS.get(config_type, PRODUCT_CONFIGS['money_back_30'])

# Environment variable options:
# RETURN_POLICY_TYPE=money_back_30    (30-day money-back guarantee)
# RETURN_POLICY_TYPE=money_back_7     (7-day money-back guarantee)  
# RETURN_POLICY_TYPE=no_returns       (No return policy) 