#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
int main(void) {
  for(int i = 1; i < 5; i++) {
    pid_t pid = fork();
    char name[10];
 
    if(pid == 0) {
      printf("Child process => PPID=%d, PID=%d\n", getppid(), getpid());
      printf("Enter user name : ");
      scanf("%s", name);
      printf("User Name : %s \n", name);
      getchar();
      exit(0);
    }
    else  {
      printf("Parent process => PID=%d\n", getpid());
      printf("\nWaiting for other user to enter name...\n");
      wait(NULL);
      printf("JOB is done!.\n");
    }
  }
 
  return EXIT_SUCCESS;
}

