// ConsoleApplication3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <stdio.h>

using namespace cv;

int main(int argc, char** argv)
{
	char* imageName = argv[1];

	Mat image;
	image = imread(imageName, 1);

	if (argc != 2 || !image.data)
	{
		printf(" No image data \n ");
		return -1;
	}

	Mat gray_image;
	cvtColor(image, gray_image, cv::COLOR_BGR2GRAY);

	imwrite("../Gray_Image.jpg", gray_image);

	namedWindow(imageName, cv::WINDOW_AUTOSIZE);
	namedWindow("Gray image", cv::WINDOW_AUTOSIZE);

	imshow(imageName, image);
	imshow("Gray image", gray_image);

	waitKey(0);

	return 0;
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
