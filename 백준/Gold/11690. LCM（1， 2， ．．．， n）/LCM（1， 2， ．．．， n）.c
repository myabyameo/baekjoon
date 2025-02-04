#include <stdio.h>
#include <stdbool.h>
#define MAX 100000001

bool che[MAX];
int main() {
	int n;
	scanf("%d", &n);
	for (int i = 2; i*i < MAX; i++) {
		if (!che[i]) {
			for (int j = i + i; j < MAX; j+=i) {
				che[j] = true;
			}
		}
	}
	long long int ans = 1;
	for (int i = 2; i < MAX; i++) {
		if (!che[i]) {
			long long tmp = 1;
			while(tmp*i<=n){
				tmp*=i;
			}
			ans = ans*tmp%4294967296;
		}
	}
	printf("%lld", ans);
}