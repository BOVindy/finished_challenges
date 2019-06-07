"""
display all outings:

event date,     event type,     cost of event,      num people attending,       cost/person,
1.) 12-1-19     bowling         1000.00             20                          20.00

outing add view:

Here are the parts of an outing:

	Event Type: (Golf, Bowling, Amusement Park, Concert)
	Number of people that attended:
	Date of event:
    what to enter, "cost" or "costper"

    total cost:

    cost per person:

    "event added"

see cost of outings:

what to view, cost by type-"cbt" or total cost-"tc"

stretch# total cost
event date,     event type,     cost of event
1.) 12-1-19     bowling         1000.00
1.) 12-1-19     bowling         1000.00
1.) 12-1-19     park         1000.00
1.) 12-1-19     golf         1000.00


Total cost for events = $4000.00


by event:

event date,     event type,     cost of event
1.) 12-1-19     bowling         1000.00
1.) 12-1-19     bowling         1000.00

total cost for bowling = 2000.00
"""






event1 = (1000, "golf")
event2 = (1000, "park")
event3 = (1400, "golf")

event_list = [event1, event2, event3]

total = 0

x = input("what type of event?")

for i in event_list:
    if i[1] == x:
        total += 1[0]
#i.eventtype = cost
print(total)


