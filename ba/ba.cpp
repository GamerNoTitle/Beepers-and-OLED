
#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <string.h>
 
using namespace std;
 
 
//待处理样本的路径
#define  TXT_PATH_NAME    "test.txt"
 
void getTxtPartName (char *partName, string txtPathName) ;
 
 
int main()
{
	//统计txt中的总行数
	ifstream countSamplesNum(TXT_PATH_NAME);
	string samplesPathName;
 
	int eachSplitGroupLineNum[100];  //保存各份的行数
	int samplesNum = 0;              //txt中的总行数
	int splitNum = 0;                //计划拆分的份数
 
	//循环读取txt的各行
	while (1) 
	{
		if (!getline(countSamplesNum,samplesPathName)) 
		{
			break;
		}
		if (samplesPathName.empty()) 
		{
			continue; 
		}
		samplesNum++;
	}
 
	cout<<"输入txt的总行数："<<samplesNum<<endl;
	cout<<"请输入拆分数量：";
	cin>>splitNum;
 
	cout<<endl<<endl<<"请依次输入"<<splitNum<<"份的行数："<<endl;
	for (int i=0; i<splitNum; i++)
	{
		cin>>eachSplitGroupLineNum[i];
	}
	cout<<endl<<endl;
 
	char  dispParams[1024];   //读入原文件的名字
	char saveNameExt[1024];   //保存新文件的名字，源文件加数字
 
	getTxtPartName(dispParams, TXT_PATH_NAME);   //从输入txt的路径获取txt文件名
 
 
	//实现拆分，文件保存
	ifstream totalSamplesPath(TXT_PATH_NAME);
	string singleSamplesPath;
 
	for (int i=0; i<splitNum; i++)
	{
		sprintf(saveNameExt, "%s_%d.txt", dispParams, i);
		FILE *labelfilename = fopen(saveNameExt, "w+t");
 
		for (int j=0; j<eachSplitGroupLineNum[i]; j++)
		{
			getline(totalSamplesPath, singleSamplesPath);
			const char* ch=singleSamplesPath.c_str();
			if (j==0)
			{
				fprintf(labelfilename, "%s", ch);
			} 
			else 
			{
				fprintf(labelfilename, "\n%s", ch);
			}
		}
 
		fclose(labelfilename);
	}
 
	system("pause");
	return 0;
}
 
 
//从txtPathName截取最后一个“\\”后与“.”之前的部分名称
void getTxtPartName (char *partName, string txtPathName) 
{
	char tmpChar1[1024]={'0',};
	char tmpChar2[1024]={'0',};
	strcpy(tmpChar1, txtPathName.c_str());
	int pathNameLen = strlen(tmpChar1); 
	int pos = pathNameLen; 
	while (pos > 0) 
	{
		pos--; 
		if (tmpChar1[pos] == '\\') 
		{
			pos++; 
			break;
		} 
	}
 
	memcpy(tmpChar2, tmpChar1 + pos, pathNameLen-pos); 
	pos = strlen(tmpChar2); 
 
	while (pos > 0) 
	{
		if (tmpChar2[pos] == '.') 
			break; 
		pos--; 
	}
 
	tmpChar2[pos] = 0; 
	sprintf(partName, "%s", tmpChar2);
}
