import pandas as pd
class Naive:
	def __init__(self):
		df = pd.read_csv("training_examples1.csv")
		
		pos_examples = df[df['PlayTennis']=='yes']
		neg_examples = df[df['PlayTennis']=='no']
		
		pos = pos_examples.shape[0]
		neg = neg_examples.shape[0]
		total = df.shape[0]

		print(pos,neg,total)

		pos1 = pos_examples[pos_examples["Outlook"]=="sunny"].shape[0]
		pos2 = pos_examples[pos_examples["Temp"]=="cool"].shape[0]
		pos3 = pos_examples[pos_examples["Humidity"]=="high"].shape[0]
		pos4 = pos_examples[pos_examples["Wind"]=="strong"].shape[0]

		print(pos1,pos2,pos3,pos4)

		neg1 = neg_examples[neg_examples["Outlook"]=="sunny"].shape[0]
		neg2 = neg_examples[neg_examples["Temp"]=="cool"].shape[0]
		neg3 = neg_examples[neg_examples["Humidity"]=="high"].shape[0]
		neg4 = neg_examples[neg_examples["Wind"]=="strong"].shape[0]

		print(neg1,neg2,neg3,neg4)

		Map_pos = (float(pos)/total)*(float(pos1)/pos)*(float(pos2)/pos)*(float(pos3)/pos)*(float(pos4)/pos)
		Map_neg = (float(neg)/total)*(float(neg1)/neg)*(float(neg2)/neg)*(float(neg3)/neg)*(float(neg4)/neg)

		print(Map_pos,Map_neg)

		pos_norm = float(Map_pos)/(Map_pos+Map_neg)
		neg_norm = float(Map_neg)/(Map_pos+Map_neg)

		print(pos_norm,neg_norm)

s = Naive()
