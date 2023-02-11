# dtas
Projekt na DTAS SL2016

## Członkowie
* Damian
* Michał
* Arkadiusz
* Dawid


## Końcówki:

###USER:

##### GET /v1/user
Wyświetla wszystkich uzytkownikow

##### GET /v1/user/{id}
Wyświetla dane użytkownika o podanym id

##### POST /v1/user
Dodawanie nowego uzytkownika, wymagania:
Nagłówek: `Content-Type: application/json`
Przykładowe request body:
`{"name":"Arek",
 "mail":"asd@ads.pl",
 "password":"arek"}`

##### PUT /v1/user/{id}
Aktualizacja użytkownika, wymagania takie jak w POST /v1/user

##### DELETE /v1/user/{id}
Usuwa użytkownika o podanym id

###POST:

##### GET /v1/post
Wyświetla wszystkie posty

##### GET /v1/post/{id}
Wyświetla dane postu o danym id

##### GET /v1/user/{author}/posts
Wyświetla posty uzytkownika o podanym id or name

##### GET /v1/post?title={title}
Wyswietla dane postu o danym tytule

##### POST /v1/post
Dodawanie nowego postu, wymagania:
Nagłówek: `Content-Type: application/json`
Przykładowe request body:
`{"title":"Moj pierwszy wpis",
 "content":"Stworzyl sie!"}`

##### DELETE /v1/post/{id}
Usuwa post o podanym id

###COMMENT

#### POST /v1/comment
Dodawanie komentarza (np. {id:null,content:'',post:{id:}}

#### PUT /v1/comment/{id}
Aktualizacja komentarza o danym id

#### GET /v1/comment
Wyświetla wszystkie komentarze

#### GET /v1/user/{id/nazwausera}/comments
Wyświetla komentarze użytkownika o danym id/nazwie

#### GET /v1/post/{postid}/comments
Wyświetla komentarze dla danego postu

#### GET /v1/comment/{id}
Wyświetla komentarz o danym id

#### DELETE /v1/comment/{id}
Usuwanie komentarza o danym id
