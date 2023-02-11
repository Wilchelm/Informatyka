#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<unistd.h>
#include<string.h>
#include<netdb.h>
#include<errno.h>
#include<arpa/inet.h>
#include<fcntl.h>

void clearString(char *s, size_t length);
int hostname_to_ip(char *  , char *);
int recv_timeout(int s , int timeout);

int main()
{
    FILE *fp;
    int comsocket,datasocket,cport,code, error;
    char rcvmsg[100],rcvdata[100], filename[50], address[50], data_address[15], user[25], password[50], buffer[50], command[80], cmd[20], param1[30], hostname[50], a1[3],a2[3],a3[3],a4[3],p1[5],p2[5], tmp[100];
    char* token;
    char* stringp;
    struct sockaddr_in servaddr, dataaddr;

	printf("Welcome to Simple FTP Client\n");
	printf("Use the \'help\' command for list of available commands\n");

    while(true)
    {
        clearString(command, 80);
        clearString(rcvmsg, 100);
        clearString(rcvdata, 100);
        clearString(cmd, 20);
        scanf("%79s", command);

        if (strcmp(command, "ls")==0)
        {

            datasocket=socket(AF_INET,SOCK_STREAM,0);
            strcpy(cmd,"PASV");
            send(comsocket,cmd, sizeof(cmd),0);

			recv(comsocket, rcvmsg, 100, 0);
			printf("%s\n", rcvmsg);
            sscanf(rcvmsg, "%d %*s %*s %*s %*c %s", &code, tmp); //teraz tmp zawiera informacje w postaci ip,ip,ip,ip,port1,port2)

            //wyłuskiwanie adresu i portu z tmp
            stringp = tmp;
            token = strsep(&stringp, ",");
            strcpy(a1, token);
            token = strsep(&stringp, ",");
            strcpy(a2, token);
            token = strsep(&stringp, ",");
            strcpy(a3, token);
            token = strsep(&stringp, ",");
            strcpy(a4, token);
            token = strsep(&stringp, ",");
            strcpy(p1, token);
            token = strsep(&stringp, ",");
            strcpy(p2, token);

            for(int i=0; i<5; i++)
            {
				if(p2[i]==')')
					p2[i]='\0';
			}

			//kod 227 oznacza potwierdzenie przejścia w tryb pasywny
            if(code == 227)
            {
				strcpy(data_address,a1);
				sprintf(data_address, "%s.%s.%s.%s",a1,a2,a3,a4);

                dataaddr.sin_family=AF_INET;
                dataaddr.sin_addr.s_addr=htonl(INADDR_ANY);
                dataaddr.sin_port=htons(atoi(p1)*256+atoi(p2));
                dataaddr.sin_addr.s_addr = inet_addr(data_address);
                if(connect(datasocket,(struct sockaddr *)&dataaddr,sizeof(dataaddr))<0)
                {
                    printf("Error in connection\n");
                    exit(0);
                }
                //połączenie się powiodło
                else
                {
                    printf("connected\n");
					clearString(cmd, 80);
					clearString(rcvmsg, 100);
					strcpy(cmd, "TYPE I"); //continuous mode
					send(comsocket,cmd, sizeof(cmd),0);
					while (recv(comsocket, rcvmsg, 100, MSG_DONTWAIT)>0)
					{
						printf("%99s\n", rcvmsg);
						clearString(rcvmsg, 100);
					}
					clearString(cmd, 80);
					strcpy(cmd, "LIST");
					send(comsocket,cmd, sizeof(cmd),0);
					recv(comsocket, rcvmsg, 100, 0);
					printf("%99s\n", rcvmsg);

					clearString(buffer, 100);
					while (recv(datasocket, buffer, 100, 0)>0)
					{
						printf("%s", buffer);
						clearString(buffer, 100);
					}
					printf("\n");

					clearString(rcvmsg, 100);
					while (recv(comsocket, rcvmsg, 100, MSG_DONTWAIT)>0)
					{
						printf("%99s", rcvmsg);
						clearString(rcvmsg, 100);
					}
					printf("\n");
				}
            }
            else
                printf("error - unhandled code\n");



        }
        else if (strcmp(command, "mkdir")==0)
        {
            printf("Specify name of directory to create: \n");
            scanf("%29s", param1);
            strcpy(cmd, "MKD ");
            strcat(cmd, param1);
            send(comsocket, cmd, sizeof(cmd), 0);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "rmdir")==0)
        {
            printf("Specify name of directory to remove: \n");
            clearString(param1, 30);
            scanf("%29s", param1);
            strcpy(cmd, "RMD ");
            strcat(cmd, param1);
            send(comsocket, cmd, sizeof(cmd), 0);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "cd")==0)
        {
            printf("Specify name of directory to switch to: \n");
            clearString(param1, 30);
            scanf("%29s", param1);
            strcpy(cmd, "CWD ");
            strcat(cmd, param1);
            send(comsocket, cmd, sizeof(cmd), 0);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "help")==0)
        {
            printf("List of available commands:\n");
            printf("login - enter username and password\n");
            printf("ls - list current directory\n");
            printf("mkdir - create directory\n");
            printf("rmdir - remove directory\n");
            printf("cd - change directory\n");
            printf("pwd - print current directory\n");
            printf("get - download file\n");
            printf("put - upload file\n");
            printf("close - terminate connection\n");
            printf("clear - clears the screen\n");
            printf("quit - close any open connections and terminate the program\n");
        }
        else if (strcmp(command, "pwd")==0)
        {
            strcpy(cmd, "PWD");
            send(comsocket, cmd, sizeof(cmd), 0);
            printf("PWD sent\n");
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "get")==0)
        {
			datasocket=socket(AF_INET,SOCK_STREAM,0);
            strcpy(cmd,"PASV");
            send(comsocket,cmd, sizeof(cmd),0);

			recv(comsocket, rcvmsg, 100, 0);
			printf("%s\n", rcvmsg);
            sscanf(rcvmsg, "%d %*s %*s %*s %*c %s", &code, tmp); //teraz tmp zawiera informacje w postaci (ip,ip,ip,ip,port1,port2)

            //wyłuskiwanie adresu i portu z tmp
            stringp = tmp;
            token = strsep(&stringp, ",");
            strcpy(a1, token);
            token = strsep(&stringp, ",");
            strcpy(a2, token);
            token = strsep(&stringp, ",");
            strcpy(a3, token);
            token = strsep(&stringp, ",");
            strcpy(a4, token);
            token = strsep(&stringp, ",");
            strcpy(p1, token);
            token = strsep(&stringp, ",");
            strcpy(p2, token);

            for(int i=0; i<5; i++)
            {
				if(p2[i]==')')
					p2[i]='\0';
			}

			//kod 227 oznacza potwierdzenie przejścia w tryb pasywny
            if(code == 227)
            {
				strcpy(data_address,a1);
				sprintf(data_address, "%s.%s.%s.%s",a1,a2,a3,a4);

                dataaddr.sin_family=AF_INET;
                dataaddr.sin_addr.s_addr=htonl(INADDR_ANY);
                dataaddr.sin_port=htons(atoi(p1)*256+atoi(p2));
                dataaddr.sin_addr.s_addr = inet_addr(data_address);
                if(connect(datasocket,(struct sockaddr *)&dataaddr,sizeof(dataaddr))<0)
                {
                    printf("Error in connection\n");
                    exit(0);
                }
                //połączenie się powiodło
                else
                {
                    printf("connected\n");
					//clearString(cmd, 80);
					//clearString(rcvmsg, 100);
					//strcpy(cmd, "TYPE I"); //continuous mode
					//send(comsocket,cmd, sizeof(cmd),0);
					//recv(comsocket, rcvmsg, 100, MSG_DONTWAIT);
				}
            }
            else
                printf("error - unhandled code\n");

            clearString(param1, 30);
            clearString(buffer, 100);
            clearString(cmd, 30);
            printf("Enter filename: ");
            scanf("%29s", param1);
            strcpy(buffer, "RETR ");
            strcat(buffer, param1);

            clearString(buffer, sizeof(buffer));
            send(comsocket, buffer, sizeof(buffer), 0);

            clearString(rcvmsg, sizeof(rcvmsg));
            recv(comsocket, rcvmsg, 99, 0);
            printf("%s\n", rcvmsg);

            fp=fopen(param1, "w");

            if (fp!=NULL)
            {
				printf("File open for write\n");

				clearString(buffer, sizeof(buffer));
				while(recv(datasocket, buffer, 99, 0)>0)
				{
					fputs(buffer, fp);
					clearString(buffer, sizeof(buffer));
				}
			}
			else
				printf("Error opening file\n");

        }
        else if (strcmp(command, "put")==0)
        {
			datasocket=socket(AF_INET,SOCK_STREAM,0);
            strcpy(cmd,"PASV");
            send(comsocket,cmd, sizeof(cmd),0);

			recv(comsocket, rcvmsg, 100, 0);
			printf("%s\n", rcvmsg);
            sscanf(rcvmsg, "%d %*s %*s %*s %*c %s", &code, tmp); //teraz tmp zawiera informacje w postaci (ip,ip,ip,ip,port1,port2)

            //wyłuskiwanie adresu i portu z tmp
            stringp = tmp;
            token = strsep(&stringp, ",");
            strcpy(a1, token);
            token = strsep(&stringp, ",");
            strcpy(a2, token);
            token = strsep(&stringp, ",");
            strcpy(a3, token);
            token = strsep(&stringp, ",");
            strcpy(a4, token);
            token = strsep(&stringp, ",");
            strcpy(p1, token);
            token = strsep(&stringp, ",");
            strcpy(p2, token);

            for(int i=0; i<5; i++)
            {
				if(p2[i]==')')
					p2[i]='\0';
			}

			//kod 227 oznacza potwierdzenie przejścia w tryb pasywny
            if(code == 227)
            {
				strcpy(data_address,a1);
				sprintf(data_address, "%s.%s.%s.%s",a1,a2,a3,a4);

                dataaddr.sin_family=AF_INET;
                dataaddr.sin_addr.s_addr=htonl(INADDR_ANY);
                dataaddr.sin_port=htons(atoi(p1)*256+atoi(p2));
                dataaddr.sin_addr.s_addr = inet_addr(data_address);
                if(connect(datasocket,(struct sockaddr *)&dataaddr,sizeof(dataaddr))<0)
                {
                    printf("Error in connection\n");
                    exit(0);
                }
                //połączenie się powiodło
                else
                {
                    printf("connected\n");
					clearString(cmd, 80);
					clearString(rcvmsg, 100);
					strcpy(cmd, "TYPE I"); //continuous mode
					send(comsocket,cmd, sizeof(cmd),0);
					while (recv(comsocket, rcvmsg, 100, MSG_DONTWAIT)>0)
					{
						printf("%s\n", rcvmsg);
						clearString(rcvmsg, 100);
					}
					clearString(cmd, 80);
					strcpy(cmd, "LIST");
					send(comsocket,cmd, sizeof(cmd),0);
					recv(comsocket, rcvmsg, 100, 0);
					printf("%s\n", rcvmsg);

					clearString(buffer, 100);
					while (recv(datasocket, buffer, 100, 0)>0)
					{
						printf("%s", buffer);
						clearString(buffer, 100);
					}
					printf("\n");

					clearString(rcvmsg, 100);
					while (recv(comsocket, rcvmsg, 100, MSG_DONTWAIT)>0)
					{
						printf("%s", rcvmsg);
						clearString(rcvmsg, 100);
					}
					printf("\n");
				}
            }
            else
                printf("error - unhandled code\n");

            strcpy(cmd, "STOR");
            send(comsocket, cmd, sizeof(cmd), 0);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "close")==0)
        {
            clearString(buffer, 100);
            strcpy (buffer, "QUIT");

            send(comsocket,buffer,sizeof(buffer),0);
            clearString(rcvmsg, 100);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "rm")==0)
        {
            printf("Specify name of file to remove: \n");
            clearString(param1, 30);
            scanf("%29s", param1);
            strcpy(cmd, "DELE");
            send(comsocket, cmd, sizeof(cmd), 0);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
        }
        else if (strcmp(command, "clear")==0)
        {
            system("clear");
        }
        else if (strcmp(command, "login")==0)
        {
			printf("Enter host name: ");
			scanf("%49s", hostname);
			//strcpy(address, "70.42.74.46"); //uo server
			printf("Enter the port: ");
			scanf("%d",&cport);
			//cport = 21;
			comsocket=socket(AF_INET,SOCK_STREAM,0);
			if(comsocket<0)
			{
				printf("Error creating command socket\n");
				exit(1);
			}
			else
				printf("Socket is created\n");

			hostname_to_ip(hostname, address);

			servaddr.sin_family=AF_INET;
			servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
			servaddr.sin_port=htons(cport);
			servaddr.sin_addr.s_addr = inet_addr(address);

			if(connect(comsocket,(struct sockaddr *)&servaddr,sizeof(servaddr))<0)
			{
				printf("Error in connection\n");
				exit(1);
			}
			else
				printf("connected\n");

			clearString(rcvmsg, 100);
			recv(comsocket, rcvmsg, 100, 0);
			printf("%s", rcvmsg);

			clearString(buffer, 100);
			printf("Login: ");
			scanf("%24s",user);
			strcpy(buffer, "USER ");
			strncat(buffer, user,sizeof(user));
			send(comsocket,buffer,sizeof(buffer),0 );

			clearString(rcvmsg, 100);
			recv(comsocket, rcvmsg, 100, 0); //sekcja dla serwerów nieanonimowych

				printf("%s", rcvmsg);

				clearString(buffer, 100);
				printf("Password: ");
				scanf("%49s",password);
				strcpy(buffer, "PASS ");
				strncat(buffer, password,sizeof(password));
				send(comsocket,buffer,sizeof(buffer),0);


			clearString(rcvmsg, 100);
			recv(comsocket, rcvmsg, 100, 0);
			printf("%s", rcvmsg);
			//tutaj klient juz jest zalogowany
        }
        else if (strcmp(command, "quit")==0)
        {
            clearString(buffer, 100);
            strcpy (buffer, "QUIT");

            send(comsocket,buffer,sizeof(buffer),0);
            clearString(rcvmsg, 100);
            recv(comsocket, rcvmsg, 100, 0);
            printf("%s\n", rcvmsg);
            exit(0);
        }
        else
        {
            printf("error - unknown command, please try again\n");
        }
    }

}

//funkcja czyszcząca string s o długości length
void clearString(char *s, size_t length)
{
     memset(s, '\0', length);
};

//funkcja zamieniająca hostname na adres IP
int hostname_to_ip(char * hostname , char* ip)
{
    struct hostent *he;
    struct in_addr **addr_list;

    if ( (he = gethostbyname( hostname ) ) == NULL)
    {
        // get the host info
        herror("gethostbyname");
        return 1;
    }

    addr_list = (struct in_addr **) he->h_addr_list;

    for(int i = 0; addr_list[i] != NULL; i++)
    {
        strcpy(ip , inet_ntoa(*addr_list[i]) );
        return 0;
    }

    return 1;
}
