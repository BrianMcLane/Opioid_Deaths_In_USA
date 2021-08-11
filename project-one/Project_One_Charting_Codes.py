# Total Deaths per State 2011-2017
yticks = [0, 1000, 2000, 3000, 4000, 5000, 
          6000, 7000, 8000, 9000, 10000, 11000, 12000]
plt.figure(figsize=(15, 8))
plt.bar(state_df.index, state_df['Death Total'], color='purple')
plt.title('Total Deaths per State 2011-2017')
plt.xticks(rotation='vertical')
plt.yticks(yticks)
plt.tight_layout()
plt.xlim(-1, 49, -.1)
plt.savefig('Total Deaths per State 2011-2017')
plt.show()

# Total Deaths State 2011-2017
yticks = [0, 1000, 2000, 3000, 4000, 5000, 
          6000, 7000, 8000, 9000, 10000, 11000, 12000]
plt.figure(figsize=(15, 8))
plt.bar(state_df.index, state_df['Death Total'], color='purple')
plt.title('Total Deaths per State 2011-2017')
plt.xticks(rotation='vertical')
plt.yticks(yticks)
plt.tight_layout()
plt.xlim(-1, 1)
plt.savefig('Total Deaths in Alabama 2011-2017')
plt.show()

#2011 Income by State
plt.figure(figsize=(20,10))
plt.bar(year_inc.index,eleven_inc, color='blue')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()

#2012 Income by State
plt.figure(figsize=(20,10))
plt.bar(twelve_inc.index, twelve_inc, color='red')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()

#2013 Income by State
plt.figure(figsize=(20,10))
plt.bar(thirteen_inc.index,thirteen_inc, color='green')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()

#2014 Income by State
plt.figure(figsize=(20,10))
plt.bar(fourteen_inc.index, fourteen_inc, color='pink')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()

#2015 Income by State
plt.figure(figsize=(20,10))
plt.bar(fifteen_inc.index,fifteen_inc, color='yellow')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()

#2016 Income by State
plt.figure(figsize=(20,10))
plt.bar(sixteen_inc.index,sixteen_inc, color='orange')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()

#2017 Income by State
plt.figure(figsize=(20,10))
plt.bar(seventeen_inc.index,seventeen_inc, color='black')
plt.xticks(rotation='vertical')
# plt.yticks(yticks)
plt.xlim(-1,49)
plt.show()


# Illinois Line chart (comparing counties)
yyticks = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
labels = ['Cook','DuPage']
plt.plot(cook['Year'], cook['Death Total'])
plt.plot(dupage['Year'], dupage['Death Total'])
plt.yticks(yyticks)
plt.legend(labels)
plt.show()