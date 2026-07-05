import secrets
import string

def generate_reference_no(ref_type="booking", length=8):
    """
    Generates a unique reference number with a type prefix.
    
    ref_type: 'booking', 'message', or 'complaint'
    """
    prefixes = {
        "booking": "bk",
        "message": "ms",
        "complaint": "cp"
    }
    
    prefix = prefixes.get(ref_type, "gn")  # 'gn' = general, fallback
    chars = string.ascii_uppercase + string.digits
    code = ''.join(secrets.choice(chars) for _ in range(length))
    
    return f"{prefix}-{code}"


