// Gets the number of words with respect to each line (line no; word total) from the text file.
// Gets the list of punctuations used in the text and the most frequently used punctuation.

#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	FILE *f,*f1;
	char ch;
	int line=0,word=0,i=0,j=0;
	char punc[100]; 

	f=fopen("trse.txt","r");
	
	while((ch=getc(f))!=EOF)
	{
		if(isspace(ch)||ch=='\t'||ch=='\n')
		{
			if(isspace(ch)||ch=='\t')
			{
				word++;
			}
			if(ch=='\n')
			{
				line++;
				printf("%d;%d|",line,word);
				word=0;
			}

		}
		
	}

	printf("\n");
	fclose(f);

	f1=fopen("trse.txt","r");
		
	while((ch=getc(f1))!=EOF)
	{
		if(ch=='!'||ch==','||ch=='.'||ch=='"'||ch==':'||ch==';'||ch=='?')
		{
			punc[i]=ch;
			i++;		
		}
	}
	printf("\n");
	fclose(f1);
	
	printf("The list of punctuations in the text are:\n");
	for(j=0;j<i;j++)
	{
		printf("%c",punc[j]);
	}
	printf("\n");

	int array[255] = {0};
	int k,max, index;
	
	for(k = 0; punc[k] != 0; k++)
	{
   		++array[punc[k]];
	}
	
	max = array[0];
	index = 0;
	for(k = 0; punc[k] != 0; k++)
	{
     	if( array[k] > max)
     	{
        	max = array[k];
      		index = k;
     	}
    }
    printf("\nThe most frequently used punctuation is: %c \n", (char)index);

	return 0;
}