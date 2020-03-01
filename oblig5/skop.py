

1) Først defineres minFunksjon(), som ikke tar noen parametere.
Inni minfunksjon finner vi en forloop som kjører en gang for hvert element i listen range(2), altså [0,1], så 2 ganger. Inni her printer den c, som er tallet 2, også sier den at b er lik 10 + a og printer b. Vi vet ikke hva a er.

Siden den sier at c = 2 og b = 10, vet vi at vi egt bare trenger å tenke på siste iterasjon for å finne ut hva verdien blir, og finne ut hva den returnerer. I tillegg så returneres ikke c. 

deretter definerer den hovedprogrammet(). 

a = 42, b = 0; printer b, b= 42, så kommer det spennende,

a = minFunksjon(), vi overser C. b = 10, b er lik b+a = 10 + 42. = 52. Så skjer det samme en gang til med at b settes til 10 og så plusses på 42.
returnerer 52. 

så printer hovedprogrammet b som er 52 og a som er 42.



forsøk2: Testet programmet nå, og så at programmet selvfølgelig crasjer i første iterasjon i minFunksjon, ettersom a aldri blir definert og er en lokal variabel i hovedprogrammet. 
