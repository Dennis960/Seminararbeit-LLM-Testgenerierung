def analyze_data_transfers(transfers):
    from collections import defaultdict
    data_transfer_summary = defaultdict(int)
    for source_ip, destination_ip, data_amount in transfers:
        data_transfer_summary[source_ip] += data_amount
    summary_list = list(data_transfer_summary.items())
    summary_list.sort(key=lambda x: (-x[1], x[0]))
    return summary_list