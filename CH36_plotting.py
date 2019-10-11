from bokeh.plotting import figure,show,output_file
output_file("plot.html")
x_categories=["a","b","c","d","e","f","g"]
x=["a","b","c","d","e"]
y=[1,2,3,4,5]
p=figure(x_range=x_categories)
p.vbar(x=x,top=y,width=0.5)
show(p)
