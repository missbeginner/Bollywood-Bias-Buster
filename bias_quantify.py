from collections import Counter

def quantify_bias(results):
    counts = Counter()
    for r in results:
        for s in r['stereotypes']:
            key = f"{r['gender']}_{s}"
            counts[key] += 1
    return dict(counts)