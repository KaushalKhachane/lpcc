%{
#include "file.tab.h"
#include <string.h>
%}

%option noyywrap

%%
[ \t\n]         ; // Ignore whitespace
[0-9]+          { yylval.ival = atoi(yytext); return NUMBER; }
\"[^\"]*\"      { yylval.sval = strdup(yytext); return STRING; } // Fixed regular expression for string
.               { return yytext[0]; }
%%

