#include <stdio.h>

int sumof(int, int); //sumof �Լ� ����

int main(){
int num_1, num_2;
int result;

printf("�� ������ �Է����ּ���. : ");
scanf("%d %d",&num_1,&num_2);

result=sumof(num_1, num_2);

printf("�� ������ ������ �� ������ ��� ������ ���� : %d �Դϴ�.",result);

return 0;
}

int sumof(int a,int b){
	int sum=0;
	for(int i=a;i<b+1;i++){
		sum+=i;
	}
return sum;
}