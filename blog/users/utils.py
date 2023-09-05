import uuid

def generate_ref_code():
    return str(uuid.uuid4()).replace("-","")[:12]