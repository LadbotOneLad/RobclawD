# =========================================================================
# NUMERIC MATH: SIMPLE AGGREGATION CHANNEL
# =========================================================================

def process(data):
    total = sum(data) if data else 0
    return {
        "type": "numeric",
        "sum": total,
        "count": len(data) if data else 0,
        "status": "OK",
    }
