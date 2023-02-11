------ usun istniejace tabele

IF OBJECT_ID('Zatrudnienia', 'U') IS NOT NULL 
drop table Zatrudnienia

IF OBJECT_ID('Wynagrodzenie', 'U') IS NOT NULL 
	drop table Wynagrodzenie
	
IF OBJECT_ID('Pracownicy', 'U') IS NOT NULL 
	drop table Pracownicy
	
	
IF OBJECT_ID('GrupyZawodowe', 'U') IS NOT NULL 
	drop table GrupyZawodowe


	IF OBJECT_ID('Oddzialy', 'U') IS NOT NULL 
	drop table Oddzialy
	
IF OBJECT_ID('Czasy', 'U') IS NOT NULL 
	drop table Czasy




------- utworz tabele


CREATE TABLE [dbo].[Czasy](
	[ID_Czasy] [int] NOT NULL,
	[Miesiac] [int] NULL,
	[Rok] [int] NULL,
	[Kwartal] [int] NULL,
CONSTRAINT [KeyCzas] PRIMARY KEY CLUSTERED 
(
	[ID_Czasy] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


CREATE TABLE [dbo].[Oddzialy](
	[ID_Oddzialu] [int] NOT NULL,
	[Skrot] [varchar](255) COLLATE Polish_CI_AS NULL,
	[Nazwa] [varchar](255) COLLATE Polish_CI_AS NULL,
 CONSTRAINT [KeyOddzialy] PRIMARY KEY CLUSTERED 
(
	[ID_Oddzialu] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[GrupyZawodowe](
	[ID_GrupyZawodowej] [int] IDENTITY(1,1) NOT NULL,
	[Skrot_GrupyZawodowej] [varchar](100) COLLATE Polish_CI_AS NULL,
	[Nazwa_GrupyZawodowej] [varchar](100) COLLATE Polish_CI_AS NULL,
 CONSTRAINT [KeyGrupyZawodowe] PRIMARY KEY CLUSTERED 
(
	[Id_GrupyZawodowej] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[Pracownicy](
	[ID_Pracownika] [int] NOT NULL,
	[RokUr] [int] NOT NULL,
	[Wyksztalcenie] [varchar](50) COLLATE Polish_CI_AS NULL,
	[Plec]  [varchar](50) COLLATE Polish_CI_AS  NULL
 CONSTRAINT [KeyPracownicy] PRIMARY KEY CLUSTERED 
(
	[ID_Pracownika] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


CREATE TABLE [dbo].[Wynagrodzenie](
	[ID_Wynagrodzenie] [int] IDENTITY(1,1) NOT NULL,
	[ID_Pracownika] [int] NOT NULL,
	[ID_GrupyZawodowej] [int] NOT NULL,
	[ID_Czasy] [int] NOT NULL,
	[ID_Oddzialu] [int] NOT NULL,
	[Brutto] [float] NULL,
	[Zasadnicze] [float] NULL,
	[Nadgodziny] [float] NULL,
	[Sta¿Pracy] [float] NULL,
	[Funkcyjny] [float] NULL,
	[DodStop] [float] NULL,
	[Inne] [float] NULL,
	[WynChorobowe] [float] NULL,
	[ZasilkiZUS] [float] NULL,
	[DniZasZUS] [int] NULL,
	[DniChor] [int] NULL,
 CONSTRAINT [ID_Wynagrodzenie] PRIMARY KEY CLUSTERED 
(
	[ID_Wynagrodzenie] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [dbo].[Wynagrodzenie] WITH CHECK ADD  CONSTRAINT [RelationshipWynagrodzeniePracownik] FOREIGN KEY([ID_Pracownika])
REFERENCES [dbo].[Pracownicy] ([ID_Pracownika])

ALTER TABLE [dbo].[Wynagrodzenie] WITH CHECK ADD  CONSTRAINT [RelationshipWynagrodzenieCzasy] FOREIGN KEY([ID_Czasy])
REFERENCES [dbo].[Czasy] ([ID_Czasy])

ALTER TABLE [dbo].[Wynagrodzenie] WITH CHECK ADD  CONSTRAINT [RelationshipWynagrodzenieOddzial] FOREIGN KEY([ID_Oddzialu])
REFERENCES [dbo].[Oddzialy] ([ID_Oddzialu])

ALTER TABLE [dbo].[Wynagrodzenie] WITH CHECK ADD  CONSTRAINT [RelationshipWynagrodzenieGrupaZawodowa] FOREIGN KEY([ID_GrupyZawodowej])
REFERENCES [dbo].[GrupyZawodowe] ([ID_GrupyZawodowej])


CREATE TABLE [dbo].[Zatrudnienia](
	[ID_Zatrudnienia] [int] IDENTITY(1,1) NOT NULL,
	[ID_Czasy] [int] NOT NULL,
	[ID_Pracownika] [int] NOT NULL,
	[TrybZatrudnienia] [varchar](50) COLLATE Polish_CI_AS NOT NULL,
	[LatStazu] [int] NOT NULL,
	[Stanowisko] [varchar](100) COLLATE Polish_CI_AS NOT NULL,
	[DzienZatrudnienia] [int] NULL,
	[MiesiacZatrudnienia] [int] NULL,
	[RokZatrudnienia] [int] NULL,
	[DzienZwolnienia] [int] NULL,
	[MiesiacZwolnienia] [int] NULL,
	[RokZwolnienia] [int] NULL,
	[PlacaEtat] [float] NULL,
	[PlacaMies] [float] NULL,
	[GodzEtatu] [float] NULL,
	[GodzZatr] [float] NULL,
	[DodFunc] [float] NULL,	
	[DodZaStopien] [float] NULL,
 CONSTRAINT [KeyZatrudnienia] PRIMARY KEY CLUSTERED 
(
	[ID_Pracownika] ASC,
	[ID_Czasy] ASC,
	[Stanowisko] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

ALTER TABLE [dbo].[Zatrudnienia] WITH CHECK ADD  CONSTRAINT [RelationshipZatrudnieniaPracownik] FOREIGN KEY([ID_Pracownika])
REFERENCES [dbo].[Pracownicy] ([ID_Pracownika])

ALTER TABLE [dbo].[Zatrudnienia] WITH CHECK ADD  CONSTRAINT [RelationshipZatrudnieniaCzas] FOREIGN KEY([ID_Czasy])
REFERENCES [dbo].[Czasy] ([ID_Czasy])