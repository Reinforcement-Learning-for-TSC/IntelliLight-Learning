import matplotlib.pyplot as plt

file = open('out2.txt', "r", encoding='utf-8')
data = file.readlines()

data_rewards = []

def get_number(split_row):
	time = 0
	reward = 0
	index_time = split_row.index('time')
	index = 0
	for v in split_row:
		if 'reward' in v:
			reward = float(split_row[index+2].split('\t')[0])
			break
		index += 1
	time = float(split_row[index_time+2].split('\t')[0])
	return {'time': time, 'reward': reward}


for row in data:
	split_row = row.split(' ')
	if 'time' in split_row:
		data_rewards.append(get_number(split_row))

final = []
for value in data_rewards:
	if value not in final:
		final.append(value)

x_values = []
y_values = []
for v in final:
	x_values.append(v['time'])
	y_values.append(v['reward'])

if __name__ == "__main__":
	print(data_rewards)
	plt.figure()
	plt.title('out - time vs reward')
	plt.plot(x_values, y_values, c='green')
	plt.tick_params(axis='both', which='major', labelsize=12)
	plt.xlabel('time', fontsize=12)
	plt.ylabel('reward', fontsize=12)
	plt.show()
