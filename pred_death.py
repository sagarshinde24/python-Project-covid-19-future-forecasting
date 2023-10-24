# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:36:06 2021

@author: sheet
"""

import operator
import json
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
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

#from data_grabbers.cases_data_grabber import CasesDataGrabber
from data_grabbers.deaths_data_grabber import DeathsDataGrabber
from models.NeuralNetModel import NeuralNetModel
from models.PolynomialRegressionModel import PolynomialRegressionModel

def grab_training_set(datagrabber_class, grab_data_from_server=True, offline_dataset_date=""):
    print(6)
    grabber = globals()[datagrabber_class]()
    dataset_date = ""

    if grab_data_from_server:
        grabber.grab_data()
    else:
        dataset_date = offline_dataset_date

        if offline_dataset_date == "":
            raise Exception("Invalid offline dataset date received. Please update the 'offline_dataset_date' configuration in the config file and try again.")
    
    filename = grabber.get_dataset_file_name(dataset_date=dataset_date)

    return np.genfromtxt("datasets/" + filename, delimiter=',').astype(np.int32)

def get_model(x, y, model_config):
    print(5)
    if model_config["model"]["type"] == "regression":
        regression_model = PolynomialRegressionModel(model_config["model_name"], model_config["model"]["polynomial_degree"])
        regression_model.train(x, y)

        return regression_model
    elif model_config["model"]["type"] == "neural_net":
        neural_net_model = NeuralNetModel(model_config["model_name"])
        neural_net_model.train(x, y, model_config["model"])
        
        return neural_net_model
    
    return None

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

def print_forecast(model_name, model, beginning_day=0, limit=10):
    print(4)
    root = tk.Tk()
    root.configure(background="seashell2")
    root.geometry("300x300")


#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (300, 300))
    root.title("Covid Future Forecasting")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
    image2 =Image.open('c5.jpeg')
    image2 =image2.resize((300,300), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
    frame_display2 = tk.LabelFrame(root, text="Predicted Death Cases", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
    frame_display2.grid(row=0, column=0, sticky='nw')
    frame_display2.place(x=0, y=0)
    next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
    next_days_pred = model.get_predictions(next_days_x)

    print("The forecast for " + model_name + " in the following " + str(limit) + " days is:")

    for i in range(9):
        for j in range(1):
               i = i + 1
               b="Day " + str(i) + ": " + str(next_days_pred[i])
               e = tk.Entry(frame_display2, width=20, fg='blue',font=('Arial',16,'bold'))
               e.place(x=500,y=500)
               e.grid(row=i, column=j)
               e.insert(END, b)
            
        #print(a)
        
    root.mainloop()
def print_stats(model_config, x, y, model):
    print(3)
    y_pred = model.get_predictions(x)

    print_forecast(model_config["model_name"], model, beginning_day=len(x), limit=model_config["days_to_predict"])

    if isinstance(model, PolynomialRegressionModel):
        print("The " + model_config["model_name"] + " model function is: f(X) = " + model.get_model_polynomial_str())

    # plot_graph(model_config["model_name"], x, y, y_pred)
    # print("")

def model_handler(model_config):
    print(2)
    training_set = grab_training_set(model_config["datagrabber_class"], model_config["grab_data_from_server"], model_config["offline_dataset_date"])
    x = training_set[:, 0].reshape(-1, 1)
    y = training_set[:, 1]
    model = get_model(x, y, model_config)

    print_stats(model_config, x, y, model)

if __name__ == "__main__":
    print(1)
    config = {}

    with open("dconfig.json", "r") as f:
        config = json.load(f)

    for model_config in config["models"]:
        if "enabled" in model_config and model_config["enabled"] == False:
            continue
        
        model_handler(model_config)
