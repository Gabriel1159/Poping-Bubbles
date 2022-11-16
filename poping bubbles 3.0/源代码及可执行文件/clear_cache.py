import pickle

record_dict = {}
time_limit_record = []
record_dict['Mike'] = 0

def cancel_record():
    with open('record\\highest_score.pkl', 'wb') as f:
        pickle.dump(record_dict, f)

def cancel_time_limit_record():
    with open('record\\time_limit.pkl', 'wb') as f:
        pickle.dump(time_limit_record, f)

if __name__ == '__main__':
    cancel_record()
    cancel_time_limit_record()