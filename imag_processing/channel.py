import cv2 as cv
import numpy as np
import downloader 
import json

def json_parse(proj_id):
    path=f"C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\{proj_id}-Data\DataSet\\{proj_id}-Metadata.json"
    f1=open(path)
    data=json.load(f1)
    s=data["PRODUCT_ID"]
    mergefinal(proj_id,s)




def mergefinal(proj_id,jres):
    blue="C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\"+str(proj_id)+"-ImageSet\\ImageSet\\"+jres+"-blue.png"
    green="C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\"+str(proj_id)+"-ImageSet\\ImageSet\\"+jres+"-green.png"
    red="C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\"+str(proj_id)+"-ImageSet\\ImageSet\\"+jres+"-red.png"
    map="C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\"+str(proj_id)+"-ImageSet\\ImageSet\\"+jres+"-mapprojected.png"
    imgb=cv.imread(blue,cv.IMREAD_UNCHANGED)
    imgg=cv.imread(green,cv.IMREAD_UNCHANGED)
    imgr=cv.imread(red,cv.IMREAD_UNCHANGED)
    imgm=cv.imread(map,cv.IMREAD_UNCHANGED)





    """ imgb=cv.imread("C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\ImageSet\\JNCE_2022229_44C00045_V01-blue.png",cv.IMREAD_UNCHANGED)
    imgg=cv.imread("C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\ImageSet\\JNCE_2022229_44C00045_V01-green.png",cv.IMREAD_UNCHANGED)
    imgr=cv.imread("C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\ImageSet\\JNCE_2022229_44C00045_V01-red.png",cv.IMREAD_UNCHANGED)
    map=cv.imread("C:\\Users\\aayus\\college\\NASA_HACK\\imag_processing\\ImageSet\\JNCE_2022229_44C00045_V01-mapprojected.png",cv.IMREAD_UNCHANGED) """
    mergetemp=cv.merge([imgb,imgg,imgr])

    #add(or blend) the images
    mergefinal = cv.addWeighted(mergetemp, 0.7, imgm, 0.3, 0)


    imgb=cv.resize(imgb,(300,300))
    imgg=cv.resize(imgg,(300,300))
    imgr=cv.resize(imgr,(300,300))
    imgm=cv.resize(imgm,(300,300))
    mergetemp=cv.resize(mergetemp,(300,300))
    mergefinal=cv.resize(mergefinal,(300,300))

    cv.imshow('mergetemp',mergetemp)
    cv.imshow('mergefinal',mergefinal)
    cv.imshow('map',imgm)
    cv.imshow('red',imgr)
    cv.imshow('green',imgg)
    cv.imshow('blue',imgb)
    cv.imwrite("mergefinal.png", mergefinal)
    cv.waitKey(0) 

json_parse(636)