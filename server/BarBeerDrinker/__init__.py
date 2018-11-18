from flask import jsonify, make_response, request, Flask, render_template, url_for, flash
from BarBeerDrinker import database

app = Flask(__name__)



@app.route('/api/drinker')
def get_drinkers():
        return render_template('drinker.html', result=database.get_drinkers())

@app.route('/api/drinker/<drinker>')
def info_on_drinker(drinker):
	result2=database.beers_ordered_most(drinker)
	r2labels=[r['consumable'] for r in result2]
	r2data=[r['amount_bought'] for r in result2]
	result3=database.spending_of_drinker(drinker)
	r3labels=[r['bar'] for r in result3]
	r3data=[r['total'] for r in result3]
	return render_template('drinker.html', text_title=drinker, result1=database.info_on_drinker(drinker), 
		r2labels=r2labels, r2data=r2data, result2=result2, title1="Most ordered consumables", max1=max(r2data)+10,
		result3=result3, r3labels=r3labels, r3data=r3data, title2="Spending Habits", max3=max(r3data)+10, result4=database.monthly_breakdown(drinker))

@app.route('/api/casinos')
def get_casino():
	return render_template('casino.html', result=database.get_casinos())

@app.route('/api/modify')
def modify():
	return render_template('modification.html')
#result is of length one to have a for loop execute only once while being distinct to each request at the same page
@app.route('/api/modify/add')
def add():
	return render_template('add.html',result = " ")

@app.route('/api/modify/add/Bars', methods=['GET','POST'])
def add_Bar():
	if request.method == 'POST':
		bar=request.form['Bar']
		casino=request.form['Casino']
		address=request.form['Address']
		city=request.form['City']
		m_hour_open=str(request.form['m_hour_open'])
		m_Min_open=str(request.form['m_Min_open'])
		m_hour_closed=str(request.form['m_hour_closed'])
		m_Min_closed=str(request.form['m_Min_closed'])

		tu_hour_open=str(request.form['tu_hour_open'])
		tu_Min_open=str(request.form['tu_Min_open'])
		tu_hour_closed=str(request.form['tu_hour_closed'])
		tu_Min_closed=str(request.form['tu_Min_closed'])

		w_hour_open=str(request.form['w_hour_open'])
		w_Min_open=str(request.form['w_Min_open'])
		w_hour_closed=str(request.form['w_hour_closed'])
		w_Min_closed=str(request.form['w_Min_closed'])

		th_hour_open=str(request.form['th_hour_open'])
		th_Min_open=str(request.form['th_Min_open'])
		th_hour_closed=str(request.form['th_hour_closed'])
		th_Min_closed=str(request.form['th_Min_closed'])

		f_hour_open=str(request.form['f_hour_open'])
		f_Min_open=str(request.form['f_Min_open'])
		f_hour_closed=str(request.form['f_hour_closed'])
		f_Min_closed=str(request.form['f_Min_closed'])

		sa_hour_open=str(request.form['sa_hour_open'])
		sa_Min_open=str(request.form['sa_Min_open'])
		sa_hour_closed=str(request.form['sa_hour_closed'])
		sa_Min_closed=str(request.form['sa_Min_closed'])

		su_hour_open=str(request.form['su_hour_open'])
		su_Min_open=str(request.form['su_Min_open'])
		su_hour_closed=str(request.form['su_hour_closed'])
		su_Min_closed=str(request.form['su_Min_closed'])

		hours=m_hour_open+m_Min_open+" "+m_hour_closed+m_Min_closed+" "+tu_hour_open+tu_Min_open+" "+tu_hour_closed+tu_Min_closed+" "+w_hour_open+w_Min_open+" "+w_hour_closed+w_Min_closed+" "+th_hour_open+th_Min_open+" "+th_hour_closed+th_Min_closed+" "+f_hour_open+f_Min_open+" "+f_hour_closed+f_Min_closed+" "+sa_hour_open+sa_Min_open+" "+sa_hour_closed+sa_Min_closed+" "+su_hour_open+su_Min_open+" "+su_hour_closed+su_Min_closed

		find_bar=database.find_bar_helper(bar)

		if len(find_bar) > 0:
			return render_template('error.html')
		else:
			insert_bar=database.insert_bar(bar, casino, address, city, hours)
			return bar
			return casino
			return address
			return city
			return hours
			return render_template('submission.html', insert_bar=insert_bar)
	else:
		return render_template('add.html',result1=" ")

@app.route('/api/modify/add/Bills')
def add_Bills():
	return render_template('add.html',result2=" ")
@app.route('/api/modify/add/Consumables')
def add_Consumables():
	return render_template('add.html',result3 = " ")
@app.route('/api/modify/add/Drinker')
def add_Drinker():
	return render_template('add.html',result4 = " ")
@app.route('/api/modify/add/Frequents')
def add_Frequents():
	return render_template('add.html',result5 = " ")
@app.route('/api/modify/add/Likes')
def add_Likes():
	return render_template('add.html',result6 = " ")
@app.route('/api/modify/add/Pays')
def add_Pays():
	return render_template('add.html',result7 = " ")
@app.route('/api/modify/add/Sells')
def add_Sells():
	return render_template('add.html',result8 = " ")

@app.route('/api/modify/update')
def update():
	return render_template('update.html',result = " ")
@app.route('/api/modify/update/Bars')
def update_Bars():
	return render_template('update.html',result1= " ")
@app.route('/api/modify/update/Bills')
def update_Bills():
	return render_template('update.html',result2= " ")
@app.route('/api/modify/update/Consumables')
def update_Consumables():
	return render_template('update.html',result3= " ")
@app.route('/api/modify/update/Drinker')
def update_Drinker():
	return render_template('update.html',result4= " ")
@app.route('/api/modify/update/Frequents')
def update_Frequents():
	return render_template('update.html',result5= " ")
@app.route('/api/modify/update/Likes')
def update_Likes():
	return render_template('update.html',result6= " ")
@app.route('/api/modify/update/Pays')
def update_Pays():
	return render_template('update.html',result7= " ")
@app.route('/api/modify/update/Sells')
def update_Sells():
	return render_template('update.html',result8= " ")

@app.route('/api/modify/delete')
def delete():
	return render_template('delete.html',result = " ")
@app.route('/api/modify/delete/Bars')
def delete_Bars():
	return render_template('delete.html',result1= " ")
@app.route('/api/modify/delete/Bills')
def delete_Bills():
	return render_template('delete.html',result3= " ")
@app.route('/api/modify/delete/Consumables')
def delete_Consumables():
	return render_template('delete.html',result3= " ")
@app.route('/api/modify/delete/Drinker')
def delete_Drinker():
	return render_template('delete.html',result4= " ")
@app.route('/api/modify/delete/Frequents')
def delete_Frequents():
	return render_template('delete.html',result5= " ")
@app.route('/api/modify/delete/Likes')
def delete_Likes():
	return render_template('delete.html',result6= " ")
@app.route('/api/modify/delete/Pays')
def delete_Pays():
	return render_template('delete.html',result7= " ")
@app.route('/api/modify/delete/Sells')
def delete_Sells():
	return render_template('delete.html',result8= " ")


@app.route('/api/modify/delete/<table>')
def delete_item(table):
	return render_template('delete.html')

@app.route('/api/casinos/<casino>')
def get_casino_info(casino):
	return render_template('casino.html', text_title=casino, result1=database.get_casino_bars(casino))

@app.route('/api/bar')
def get_bars():
	return render_template('bar.html', result=database.get_bars())

@app.route('/api/bar/<bar>', methods=['GET'])
def top_spender(bar):
	result1=database.top_spenders(bar)
	r1labels=[r['Name'] for r in result1]
	r1data=[r['total'] for r in result1]
	result2=database.top_beers(bar)
	r2labels=[r['consumable'] for r in result2]
	r2data=[r['amount_sold'] for r in result2]
	result3=database.top_consumables(bar)
	r3labels=[r['Manufacturer'] for r in result3]
	r3data=[r['num_sold'] for r in result3]
	return render_template('bar.html', text_title=bar, result1=result1, r1data=r1data, r1labels=r1labels, title1="Top Spenders", max1=max(r1data)+10,
		result2=result2, r2labels=r2labels, r2data=r2data, title2="Top Consumables", max2=max(r2data)+10,
		result3=result3, r3labels=r3labels, r3data=r3data, title3="Top Manufacturers", max3=max(r3data)+10)

@app.route('/api/consumable')
def get_consumables():
	return render_template('beer.html', result=database.get_consumables())

@app.route('/api/consumable/<consumable>')
def consumables_sold_most(consumable):
	return render_template('beer.html', text_title=consumable, result1=database.consumable_sold_most(consumable), result2=database.drinkers_who_like(consumable))

@app.route('/submission', methods=['GET', 'POST'])
def submission():
	return render_template('submission.html')

@app.route('/')
def hello_world():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
 
