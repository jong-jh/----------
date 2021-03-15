#include <stdio.h>

int sumof(int, int); //sumof 함수 정의

int main(){
int num_1, num_2;
int result;

printf("두 정수를 입력해주세요. : ");
scanf("%d %d",&num_1,&num_2);

result=sumof(num_1, num_2);

printf("두 정수를 포함한 그 사이의 모든 정수의 합은 : %d 입니다.",result);

return 0;
}

int sumof(int a,int b){
	int sum=0;
	for(int i=a;i<b+1;i++){
		sum+=i;
	}
return sum;
}