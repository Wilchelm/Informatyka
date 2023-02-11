#include<iostream>

using namespace std;

int merge(int arr[],int left[],int right[],int l,int r)
{
    int i=0,j=0,count=0;
    while(i<l || j<r)
    {
        if(i==l)
        {
            arr[i+j]=right[j];
            j++;
        }
        else if(j==r)
        {
            arr[i+j]=left[i];
            i++;
        }
        else if(left[i]<=right[j])
        {
            arr[i+j]=left[i];
            i++;
        }
        else
        {
            arr[i+j]=right[j];
            count+=l-i;
            j++;
        }
    }
    return count;
}

int inversions(int arr[],int high)
{
    if(high<1)
        return 0;

    int mid=(high+1)/2;
    int left[mid];
    int right[high-mid+1];

    int i,j;
    for(i=0;i<mid;i++)
        left[i]=arr[i];


    for(i=high-mid,j=high;j>=mid;i--,j--)
        right[i]=arr[j];

return inversions(left,mid-1) + inversions(right,high-mid) + merge(arr,left,right,mid,high-mid+1);
}

int main()
{
	int d;
	cin >> d;
	for(int j=0 ; j<d;j++)
    {
		int n;
		cin >> n;
	    int arr[n];
	    for(int i=0 ; i<n;i++)
		    {
		    	cin >> arr[i];
			}
	    printf("%d ",inversions(arr,n-1));
	}
    return 0;
}
