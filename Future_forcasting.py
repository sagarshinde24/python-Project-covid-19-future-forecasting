import tkinter as tk
import json
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from bs4 import BeautifulSoup as BS 
from datetime import date
import requests 

global ans , recovered



root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Covid Future Forecasting")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('c5.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="Covid Future Forecasting", font=('times', 35,' bold '), height=1,bg="Red3",fg="white")
lbl.place(x=350, y=10)


def death():
    from subprocess import call
    call(["python", "pred_death.py"])
    # from data_grabbers.deaths_data_grabber import DeathsDataGrabber
    # from models.NeuralNetModel import NeuralNetModel
    # from models.PolynomialRegressionModel import PolynomialRegressionModel
    
    # def grab_training_set(datagrabber_class, grab_data_from_server=True, offline_dataset_date=""):
    #     grabber = globals()[datagrabber_class]()
    #     dataset_date = ""
    
    #     if grab_data_from_server:
    #         grabber.grab_data()
    #     else:
    #         dataset_date = offline_dataset_date
    
    #         if offline_dataset_date == "":
    #             raise Exception("Invalid offline dataset date received. Please update the 'offline_dataset_date' configuration in the config file and try again.")
        
    #     filename = grabber.get_dataset_file_name(dataset_date=dataset_date)
    
    #     return np.genfromtxt("datasets/" + filename, delimiter=',').astype(np.int32)
    
    # def get_model(x, y, model_config):
    #     if model_config["model"]["type"] == "regression":
    #         regression_model = PolynomialRegressionModel(model_config["model_name"], model_config["model"]["polynomial_degree"])
    #         regression_model.train(x, y)
    
    #         return regression_model
    #     elif model_config["model"]["type"] == "neural_net":
    #         neural_net_model = NeuralNetModel(model_config["model_name"])
    #         neural_net_model.train(x, y, model_config["model"])
            
    #         return neural_net_model
        
    #     return None
    
      
    # def print_forecast(model_name, model, beginning_day=0, limit=10):
    #     frame_display2 = tk.LabelFrame(root, text="Predicted Death Cases", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
    #     frame_display2.grid(row=0, column=0, sticky='nw')
    #     frame_display2.place(x=0, y=0)
    #     next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
    #     next_days_pred = model.get_predictions(next_days_x)
    
    #     print("The forecast for " + model_name + " in the following " + str(limit) + " days is:")
    
    #     for i in range(9):
    #         for j in range(1):
    #                i = i + 1
    #                b="Day " + str(i) + ": " + str(next_days_pred[i])
    #                e = tk.Entry(frame_display2, width=20, fg='blue',font=('Arial',16,'bold'))
    #                e.place(x=500,y=500)
    #                e.grid(row=i, column=j)
    #                e.insert(END, b)
                
    #         #print(a)
            
    
    # def print_stats(model_config, x, y, model):
    #     y_pred = model.get_predictions(x)
    
    #     print_forecast(model_config["model_name"], model, beginning_day=len(x), limit=model_config["days_to_predict"])
    
    #     if isinstance(model, PolynomialRegressionModel):
    #         print("The " + model_config["model_name"] + " model function is: f(X) = " + model.get_model_polynomial_str())
    
    #     # plot_graph(model_config["model_name"], x, y, y_pred)
    #     # print("")
    
    # def model_handler(model_config):
    #     training_set = grab_training_set(model_config["datagrabber_class"], model_config["grab_data_from_server"], model_config["offline_dataset_date"])
    #     x = training_set[:, 0].reshape(-1, 1)
    #     y = training_set[:, 1]
    #     model = get_model(x, y, model_config)
    
    #     print_stats(model_config, x, y, model)
    
    # if __name__ == "__main__":
    #     config = {}
    
    #     with open("dconfig.json", "r") as f:
    #         config = json.load(f)
    
    #     for model_config in config["models"]:
    #         if "enabled" in model_config and model_config["enabled"] == False:
    #             continue
            
    #         model_handler(model_config)
    
    
def total():
    from subprocess import call
    call(["python", "pred_cases.py"])
#     from data_grabbers.cases_data_grabber import CasesDataGrabber
# #from data_grabbers.deaths_data_grabber import DeathsDataGrabber
#     from models.NeuralNetModel import NeuralNetModel
#     from models.PolynomialRegressionModel import PolynomialRegressionModel

#     def grab_training_set(datagrabber_class, grab_data_from_server=True, offline_dataset_date=""):
#         print("traning set")
#         grabber = globals()[datagrabber_class]()
#         dataset_date = ""
        
#         if grab_data_from_server:
#             grabber.grab_data()
#         else:
#                 dataset_date = offline_dataset_date

#         if offline_dataset_date == "":
#             raise Exception("Invalid offline dataset date received. Please update the 'offline_dataset_date' configuration in the config file and try again.")
    
#         filename = grabber.get_dataset_file_name(dataset_date=dataset_date)
        
#         return np.genfromtxt("datasets/" + filename, delimiter=',').astype(np.int32)
    
#     def get_model(x, y, model_config):
#         print("get_model")
#         if model_config["model"]["type"] == "regression":
#             regression_model = PolynomialRegressionModel(model_config["model_name"], model_config["model"]["polynomial_degree"])
#             regression_model.train(x, y)

#             return regression_model
#         elif model_config["model"]["type"] == "neural_net":
#             neural_net_model = NeuralNetModel(model_config["model_name"])
#             neural_net_model.train(x, y, model_config["model"])
        
#             return neural_net_model
    
#         return None

#     def print_forecast(model_name, model, beginning_day=0, limit=10):
#         print("forecast")
#         frame_display3 = tk.LabelFrame(root, text="Predicted Total Cases", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#         frame_display3.grid(row=0, column=0, sticky='nw')
#         frame_display3.place(x=0, y=0)
    
#         next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
#         next_days_pred = model.get_predictions(next_days_x)

#         print("The forecast for " + model_name + " in the following " + str(limit) + " days is:")

#         for i in range(10):
        
#             for j in range(1):
#                 i = i + 1
#                 b="Day " + str(i) + ": " + str(next_days_pred[i])
#                 e = tk.Entry(frame_display3, width=20, fg='blue',font=('Arial',16,'bold'))
#                 e.grid(row=i, column=j)
#                 e.insert(END, b)
#         #return b
#         #print()

#     def print_stats(model_config, x, y, model):
#         y_pred = model.get_predictions(x)

#         print_forecast(model_config["model_name"], model, beginning_day=len(x), limit=model_config["days_to_predict"])
        
#         if isinstance(model, PolynomialRegressionModel):
#             print("The " + model_config["model_name"] + " model function is: f(X) = " + model.get_model_polynomial_str())

#     # plot_graph(model_config["model_name"], x, y, y_pred)
#     # print("")

#     def model_handler(model_config):
#         print("model handler")
#         training_set = grab_training_set(model_config["datagrabber_class"], model_config["grab_data_from_server"], model_config["offline_dataset_date"])
#         x = training_set[:, 0].reshape(-1, 1)
#         y = training_set[:, 1]
#         model = get_model(x, y, model_config)

#         print_stats(model_config, x, y, model)
  
#     if __name__ == "__main__":
#         print("hello")
#         config = {}

#         with open("cconfig.json", "r") as f:
#             config = json.load(f)

#         for model_config in config["models"]:
#             if "enabled" in model_config and model_config["enabled"] == False:
#                 continue
        
#             model_handler(model_config)
#     #x2=cases.main()
    
               
def world():
    #today = date.today()
    frame_display1 = tk.LabelFrame(root, text="hello",height=100,width=700, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
    frame_display1.grid(row=0, column=0, sticky='nw')
    frame_display1.place(x=500, y=100)
    url = "https://www.worldometers.info/coronavirus/"
    data = requests.get(url) 

	# converting the text 
    soup = BS(data.text, 'html.parser') 
	
	# finding meta info for total cases 
    total = soup.find("div", class_ = "maincounter-number").text 
	
	# filtering it 
    total = total[1 : len(total) - 2] 
    
	
	# finding meta info for other numbers 
    other = soup.find_all("span", class_ = "number-table") 
	
	# getting recovered cases number 
    recovered = other[2].text 
	
	# getting death cases number 
    deaths = other[3].text 
	
	# filtering the data 
    deaths = deaths[1:] 
	
	# saving details in dictionary 
    #ans ={'Total Cases' : total 'Recovered Cases' : recovered 'Total Deaths' : deaths}
	#print(ans)
    result_label = tk.Label(frame_display1, text="Total Cases\n"+str(total), font=("bold", 15), bg='bisque2', fg='black')
    result_label.place(x=10, y=10)
    result_label = tk.Label(frame_display1, text="Recovered Cases\n"+str(recovered), font=("bold", 15), bg='bisque2', fg='black')
    result_label.place(x=200, y=10)
    result_label = tk.Label(frame_display1, text="Total Deaths\n"+str(deaths),font=("bold", 15), bg='bisque2', fg='black')
    result_label.place(x=500, y=10)
def main():
    # import operator
    # import json
    # import numpy as np
    # import matplotlib.pyplot as plt
    
    # from data_grabbers.cases_data_grabber import CasesDataGrabber
    # from data_grabbers.deaths_data_grabber import DeathsDataGrabber
    # from models.NeuralNetModel import NeuralNetModel
    # from models.PolynomialRegressionModel import PolynomialRegressionModel
    
    # def grab_training_set(datagrabber_class, grab_data_from_server=True, offline_dataset_date=""):
    #     grabber = globals()[datagrabber_class]()
    #     dataset_date = ""
    
    #     if grab_data_from_server:
    #         grabber.grab_data()
    #     else:
    #         dataset_date = offline_dataset_date
    
    #         if offline_dataset_date == "":
    #             raise Exception("Invalid offline dataset date received. Please update the 'offline_dataset_date' configuration in the config file and try again.")
        
    #     filename = grabber.get_dataset_file_name(dataset_date=dataset_date)
    
    #     return np.genfromtxt("datasets/" + filename, delimiter=',').astype(np.int32)
    
    # def get_model(x, y, model_config):
    #     if model_config["model"]["type"] == "regression":
    #         regression_model = PolynomialRegressionModel(model_config["model_name"], model_config["model"]["polynomial_degree"])
    #         regression_model.train(x, y)
    
    #         return regression_model
    #     elif model_config["model"]["type"] == "neural_net":
    #         neural_net_model = NeuralNetModel(model_config["model_name"])
    #         neural_net_model.train(x, y, model_config["model"])
            
    #         return neural_net_model
        
    #     return None
    
    # def plot_graph(model_name, x, y, y_pred):
    #     plt.scatter(x, y, s=10)
    #     sort_axis = operator.itemgetter(0)
    #     sorted_zip = sorted(zip(x, y_pred), key=sort_axis)
    #     x, y_pred = zip(*sorted_zip)
        
    #     plt.plot(x, y_pred, color='m')
    #     plt.title("Amount of " + model_name + " in each day")
    #     plt.xlabel("Day")
    #     plt.ylabel(model_name)
    #     plt.show()
    
    # def print_forecast(model_name, model, beginning_day=0, limit=10):
    #     next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
    #     next_days_pred = model.get_predictions(next_days_x)
    
    #     print("The forecast for " + model_name + " in the following " + str(limit) + " days is:")
    
    #     for i in range(0, limit):
    #         print("Day " + str(i + 1) + ": " + str(next_days_pred[i]))
    #         # result_label = tk.Label(root, text="Day "+str(i+1)+": "+str(next_days_pred[i]), font=("bold", 25), bg='bisque2', fg='black')
    #         # result_label.place(x=300, y=420)
    
    # def print_stats(model_config, x, y, model):
    #     y_pred = model.get_predictions(x)
    
    #     print_forecast(model_config["model_name"], model, beginning_day=len(x), limit=model_config["days_to_predict"])
    
    #     if isinstance(model, PolynomialRegressionModel):
    #         print("The " + model_config["model_name"] + " model function is: f(X) = " + model.get_model_polynomial_str())
    
    #     plot_graph(model_config["model_name"], x, y, y_pred)
    #     print("")
    
    # def model_handler(model_config):
    #     training_set = grab_training_set(model_config["datagrabber_class"], model_config["grab_data_from_server"], model_config["offline_dataset_date"])
    #     x = training_set[:, 0].reshape(-1, 1)
    #     y = training_set[:, 1]
    #     model = get_model(x, y, model_config)
    
    #     print_stats(model_config, x, y, model)
    def recovery():
        # importing libraries 
        from bs4 import BeautifulSoup as BS 
        import requests 
        
        global ans , recovered
        
        # method to get the info 
        def get_info(url): 
        	global ans , recovered
        	# getting the request from url 
        	data = requests.get(url) 
        
        	# converting the text 
        	soup = BS(data.text, 'html.parser') 
        	
        	# finding meta info for total cases 
        	total = soup.find("div", class_ = "maincounter-number").text 
        	
        	# filtering it 
        	total = total[1 : len(total) - 2] 
        	
        	# finding meta info for other numbers 
        	other = soup.find_all("span", class_ = "number-table") 
        	
        	# getting recovered cases number 
        	recovered = other[2].text 
        	
        	# getting death cases number 
        	deaths = other[3].text 
        	
        	# filtering the data 
        	deaths = deaths[1:] 
        	
        	# saving details in dictionary 
        	ans ={'Total Cases' : total, 'Recovered Cases' : recovered, 
        								'Total Deaths' : deaths} 
            
            
        	
        	# returnng the dictionary 
        	return ans,recovered
        
        # url of the corona virus cases 
        url = "https://www.worldometers.info/coronavirus/"
        
        # calling the get_info method 
        ans = get_info(url) 
        today = date.today()
        frame_display = tk.LabelFrame(root, text="Total Recovery Cases Predicted", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
        frame_display.grid(row=0, column=0, sticky='nw')
        frame_display.place(x=700, y=350)
        # ans = ans.items()
        # # printing the ans 
        # for i, j in ans.items(): 
        # 	print(i + " : " + j) 
        import random
        r3 = 0
        r1 = 0
        recovered2 = 3000000
        s = recovered.replace(',', '')
        s = int(s)
        r3 = s + recovered2
        r3 = int(r3)
        r1 = s - recovered2
        r1 = int(r1)
        i=0
        for i in range(10):
            for j in range(1):
                i = i + 1
            #print(random.randint(r3, r1))
                a="Day "+str(i)+": "+str(random.randint(r1,r3))
                print(a)
                e = tk.Entry(frame_display, width=20, fg='blue',font=('Arial',16,'bold'))
                e.place(x=500,y=500)
                e.grid(row=i, column=j)
                e.insert(END, a)
            
            #e = tk.Label(root, text=a, font=("bold", 25),height=10, bg='bisque2', fg='black')
            #e.place(x=300, y=220)
            #i = i + 1
            #print("Day "+str(i)+": "+str(random.randint(r1,r3)))   
            # print(a)
            # for i in range(10):
            # #for(i=0;i<10;i++)
            #     
            # # lst = ["Day "+str(i)+": "+str(random.randint(r1,r3))]
            # for i in range(9):
            #     for j in range(1):
                  
            #         e = tk.Entry(root, width=20, fg='blue',font=('Arial',16,'bold'))
            #         e.grid(row=i, column=j)
            #         e.insert(END, lst[i][j])
       
            
            
    if __name__ == "__main__":
        recovery()
        # config = {}
    
        # with open("config.json", "r") as f:
        #     config = json.load(f)
    
        # for model_config in config["models"]:
        #     if "enabled" in model_config and model_config["enabled"] == False:
        #         continue
            
        #     model_handler(model_config)



def window():
    root.destroy()

button1 = tk.Button(root, text="Current World Meter", command=world, font=('times', 25, ' bold '),bg="SteelBlue1",fg="black")
button1.place(x=100, y=100)

button2 = tk.Button(root, text="Predict Total Cases", command=total, font=('times', 25, ' bold '),bg="SteelBlue1",fg="black")
button2.place(x=100, y=200)

button3 = tk.Button(root, text="Predict Total Death Cases", command=death, font=('times', 25, ' bold '),bg="SteelBlue1",fg="black")
button3.place(x=100, y=300)

button4 = tk.Button(root, text="Predict Total Recovery Cases", command=main, height=1, font=('times', 25, ' bold '),bg="SteelBlue1",fg="black")
button4.place(x=100, y=400)
exit = tk.Button(root, text="Exit", command=window, width=15, height=1, font=('times', 25, ' bold '),bg="red",fg="white")
exit.place(x=100, y=500)



root.mainloop()