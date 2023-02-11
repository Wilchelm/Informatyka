#loading libraries
library(shiny)
require(shinydashboard)
library(ggplot2)
library(dplyr)
library(png)

#https://www.kaggle.com/lava18/google-play-store-apps
#https://www.kaggle.com/abcsds/pokemon

################################################################################
############################## POKEMONS LOADING  ###############################
################################################################################
pokemon <- read.csv('./upload/Pokemony.csv', stringsAsFactors = F, header=TRUE, sep=',')[ ,2:13]
pokemon[[3]] <- gsub("^", "-", pokemon[[3]])
pokemon[[3]] <- gsub("-B", "B", pokemon[[3]])
pokemon[[3]] <- gsub("-D", "D", pokemon[[3]])
pokemon[[3]] <- gsub("-E", "E", pokemon[[3]])
pokemon[[3]] <- gsub("-F", "F", pokemon[[3]])
pokemon[[3]] <- gsub("-G", "G", pokemon[[3]])
pokemon[[3]] <- gsub("-I", "I", pokemon[[3]])
pokemon[[3]] <- gsub("-N", "N", pokemon[[3]])
pokemon[[3]] <- gsub("-P", "P", pokemon[[3]])
pokemon[[3]] <- gsub("-R", "R", pokemon[[3]])
pokemon[[3]] <- gsub("-S", "S", pokemon[[3]])
pokemon[[3]] <- gsub("-W", "W", pokemon[[3]])

types1 <- pokemon[2]
types2 <- pokemon[3]
types1 <- unique(types1)
types2 <- unique(types2)
types1 <- sort(types1[,])
types2 <- sort(types2[,])

count_mega <- length(grep("Mega", pokemon[[1]], perl=TRUE, value=TRUE))
count_pokemon <- length(pokemon[[1]])
count_legendary <- length(grep("True", pokemon[[12]], perl=TRUE, value=TRUE))
################################################################################
############################## GG STORE LOADING  ###############################
################################################################################
googleplaystore <- read.csv('./upload/googleplaystore.csv', stringsAsFactors = F, header=TRUE, sep=',')

category<-googleplaystore[[2]]
category<-unique(category)
category<-category[1:33]
category<-sort(category)
'
i=1
lpom=list(seq(1:length(category)))
spom = "Category , Count"
write(spom,file = "./upload/category_count.csv")
while (i<=length(category)){
  j=1
  licz=0
  while(j<=length(googleplaystore[[2]])){
    if (googleplaystore[[2]][j]==category[i]){
      licz=licz+1
    }
    j=j+1
  }
  lpom[i]=licz
  
  spom=paste(category[i],",",lpom[i])
  write(spom,file = "./upload/category_count.csv",append = TRUE)
  
  i=i+1
}
'
blabla1 <- read.csv('./upload/category_count.csv', stringsAsFactors = F, header=TRUE, sep=',')
android_ver<-sort(unique(googleplaystore[[13]]))
android_ver<-android_ver[1:33]
'
i=1
lpom=list(seq(1:length(android_ver)))
spom = "And_ver , Count"
write(spom,file = "./upload/and_ver_count.csv")
while (i<=length(android_ver)){
  j=1
  licz=0
  while(j<=length(googleplaystore[[13]])){
    if (googleplaystore[[13]][j]==android_ver[i]){
      licz=licz+1
    }
    j=j+1
  }
  lpom[i]=licz
  
  spom=paste(android_ver[i],",",lpom[i])
  write(spom,file = "./upload/and_ver_count.csv",append = TRUE)
  
  i=i+1
}
'
blabla2 <- read.csv('./upload/and_ver_count.csv', stringsAsFactors = F, header=TRUE, sep=',')
content_rating<-sort(unique(googleplaystore[[9]]))
content_rating<-content_rating[1:6]
'
i=1
lpom=list(seq(1:length(content_rating)))
spom = "Content_rating , Count"
write(spom,file = "./upload/content_rating_count.csv")
while (i<=length(content_rating)){
  j=1
  licz=0
  while(j<=length(googleplaystore[[9]])){
    if (googleplaystore[[9]][j]==content_rating[i]){
      licz=licz+1
    }
    j=j+1
  }
  lpom[i]=licz
  
  spom=paste(content_rating[i],",",lpom[i])
  write(spom,file = "./upload/content_rating_count.csv",append = TRUE)
  
  i=i+1
}
'
blabla3 <- read.csv('./upload/content_rating_count.csv', stringsAsFactors = F, header=TRUE, sep=',')
googlestat=c('Android Versions','Categories','Content Ratings')
################################################################################
################################################################################
#################################     UI     ###################################
################################################################################
################################################################################

#Dashboard header carrying the title of the dashboard
header <- dashboardHeader(title = "Shiny R", disable = FALSE)  

#Sidebar content of the dashboard
sidebar <- dashboardSidebar(
  sidebarMenu(
    h1(""),
    tags$style(".topimg {
                            margin-left:20%;
                          }"),
    div(class="topimg",img(src='pokemon_icon.png',width="70%")),
    #img(src='pokemon_icon.png', align = "center", height=128),
    menuItem("Pokemons Statistics", tabName = "pokemonStatistic"),
    menuItem("Pokemons Type Plot", tabName = "pokemonTypePlot"),
    menuItem("Pokemons Table", tabName = "tablePokemon"),
    div(class="topimg",img(src='google_play_icon.png',width="70%")),
    menuItem("Googleplay Store Statistic", tabName = "googleplaystoreStatistic", icon = icon("dashboard")),
    menuItem("Googleplay Store Plots", tabName = "GoogleplaystorePlots", icon = icon("dashboard")),
    menuItem("Googleplay Store Table", tabName = "tableGoogleplaystore", icon = icon("dashboard"))
  )
)

# Body content
body <- dashboardBody(
  tabItems(
    tabItem(tabName = "tablePokemon",
            fluidPage(
              fluidRow(column(12, dataTableOutput('table1')))
            )
    ),
    
    tabItem(tabName = "pokemonTypePlot", 
            box(
              title = "Select Pokemon Type:",
              status = "primary",
              solidHeader = TRUE,
              collapsible = TRUE,
              selectInput("selectedtypes1", "Pokemon type 1:", choices=types1, selected = types1[1]),
              h4("and"),
              selectInput("selectedtypes2", "Pokemon type 2:", choices=types2, selected = types2[1]),
              height = "230px"
            ),
            
            box(
              title = "Select Pokemon Stat:",
              status = "primary",
              solidHeader = TRUE ,
              collapsible = TRUE,
              selectInput("selectedstat1", "Pokemon  stat:", choices=colnames(pokemon[4:10])),
              height = "230px"
            ),
    
            plotOutput("plot11", height = 300)
    ), 
    
    tabItem(tabName = "pokemonStatistic",
            fluidRow(
              tags$head(tags$style(HTML(".small-box {height: 120px}"))),
              valueBox(count_pokemon, "Quantity of Pokemons", color = "yellow"),
              
              # Dynamic valueBoxes
              valueBox(count_legendary, "Quantity of Legendary Pokemons", color = "red"),
              
              valueBox(count_mega, "Quantity of Pokemons with Mega Evolution", color = "green")
            ),
            
            box(
              title = "Select Pokemon Type:"
              ,status = "primary"
              ,solidHeader = TRUE ,
              selectInput("selectedtypes11", "Pokemon type 1:", choices=types1),
              h4("and"),
              selectInput("selectedtypes12", "Pokemon type 2:", choices=types2),
              height = "230px",
              width = "10px"
            ),valueBoxOutput("outputbox1", width = "100%")
    ),
    
    tabItem(tabName = "tableGoogleplaystore",
            fluidPage(fluidRow(dataTableOutput('table2')))
    ),
    
    tabItem(tabName = "GoogleplaystorePlots",
            selectInput("region", "Select:",choices=googlestat),
            hr(),
            plotOutput(outputId = "distPlot", height = 500)
    ), 
    
    tabItem(tabName = "googleplaystoreStatistic",
            fluidRow(
              tags$head(tags$style(HTML(".small-box {height: 120px}"))),
              valueBoxOutput("vbox81",  width = 6),
              valueBoxOutput("vbox82",  width = 6)
            ),
            fluidRow(
              tags$head(tags$style(HTML(".small-box {height: 120px}"))),
              box(
                title = "Select Category :"
                ,status = "primary"
                ,solidHeader = TRUE ,
                selectInput("selectedtypes165","Category:",  choices=unique(googleplaystore[2])),
                height = "120px", width = "100%"
              )
            ),
            fluidRow(
              tags$head(tags$style(HTML(".small-box {height: 120px}"))),
              valueBoxOutput("vbox79", "Best Rated App")
            ),
            fluidRow(
              tags$head(tags$style(HTML(".small-box {height: 120px}"))),
              valueBoxOutput("vbox80", "Best Rated App")
            )
    )
  )
)

ui <- dashboardPage(title = 'Shiny R', header, sidebar, body, skin='black')
################################################################################
################################################################################
###############################     SERVER     #################################
################################################################################
################################################################################
server <- function(input, output) { 
 
  output$table2 <- renderDataTable(googleplaystore,options = list(scrollX = TRUE))
  
  output$table1 <- renderDataTable(pokemon)
  

  
  
  
  output$outputbox1 <- renderValueBox({
    #input$selectedtypes1
    #input$selectedtypes2
    licz = 0
    
    i=1
    while (i<=length(pokemon[[2]])){
      if (pokemon[[2]][i] ==input$selectedtypes11 && pokemon[[3]][i] ==input$selectedtypes12)
      {licz=licz+1}
      i=i+1
    }
    
    napis = paste("Quantity of Pokemons with Type 1:", input$selectedtypes11)
    napis = paste(napis, "and Type 2:")
    napis = paste(napis, input$selectedtypes12)
    valueBox(
      licz,
      napis
    )
  })
  
  output$plot11 <- renderPlot({
    pom=input$selectedstat1
    l=list()
    i=1
    while (i<=length(pokemon[[2]])){
      if (pokemon[[2]][i] ==input$selectedtypes1 && pokemon[[3]][i] ==input$selectedtypes2)
      {
        l<-c(l,pokemon[[pom]][i])
      }
      i=i+1
    }
    pom2=length(l)
    if (pom2 != 0){
      maks=max(sapply(l, max))
      pom3 = which(pokemon[[2]]==input$selectedtypes1 & pokemon[[3]]==input$selectedtypes2 & pokemon[[pom]]==maks)
      napis = paste( pokemon[[1]][pom3],"is the best Pokemon with Type 1:")
      napis = paste(napis, input$selectedtypes11)
      napis = paste(napis, "and Type 2:")
      napis = paste(napis, input$selectedtypes12)
      napis = paste(napis, "with stat:")
      napis = paste(napis, maks)
      plot(x=seq(1:pom2),y=l, xlab = "Quantity",ylab = pom,title(napis),col = "#ffffff")
      lines(x=seq(1:pom2),y=l,col = "#75AADB")
    }
  })
  
  output$distPlot <- renderPlot({
    if (input$region == 'Categories'){
      p1<-ggplot(data=blabla1, aes(x=Category, y=Count, fill=factor(Category)))+ 
        geom_bar(position = "dodge", stat = "identity") + ylab("Count") +
        xlab("Category") + theme(legend.position="bottom" 
                                 ,plot.title = element_text(size=15, face="bold")) + 
        ggtitle("Count Apps by Category") + labs(fill = "Category")
    
      p1 + theme(axis.text.x = element_blank(), axis.title.x = element_blank())
      print (p1)
    }
    if (input$region == 'Content Ratings'){
      p3<-ggplot(data=blabla3, aes(x=Content_rating, y=Count, fill=factor(Content_rating)))+ 
        geom_bar(position = "dodge", stat = "identity") + ylab("Count") +
        xlab("Content Rating") + theme(legend.position="bottom" 
                                       ,plot.title = element_text(size=15, face="bold")) + 
        ggtitle("Count Apps by Content Rating") + labs(fill = "Content Rating")
      
      p3 + theme(axis.text.x = element_blank(), axis.title.x = element_blank())
      print (p3)
    }
    if (input$region == 'Android Versions'){
      p2<-ggplot(data=blabla2, aes(x=And_ver , y=Count, fill=factor(And_ver)))+ 
        geom_bar(position = "dodge", stat = "identity") + ylab("Count") +
        xlab("Android version ") + theme(legend.position="bottom" 
                                 ,plot.title = element_text(size=15, face="bold")) + 
        ggtitle("Count Apps by Android version") + labs(fill = "Android Version")
      
      p2 + theme(axis.text.x = element_blank(), axis.title.x = element_blank())
      print (p2)
    }
  })
  
  output$vbox79 <- renderValueBox({
  
    x<-which(googleplaystore[2]==input$selectedtypes165)
    pomtabgoogle<-googleplaystore[x,]

    pom <- pomtabgoogle[[1]][order(pomtabgoogle[,4], decreasing = TRUE)[1]]
    napis = "Best Rating App by Category"
    valueBox(pom,napis, color = "green")
  })
  output$vbox80 <- renderValueBox({
    
    x<-which(googleplaystore[2]==input$selectedtypes165)
    pomtabgoogle<-googleplaystore[x,]
    
    pom <- pomtabgoogle[[1]][order(pomtabgoogle[,6], decreasing = TRUE)[1]]
    napis = "Best Popular App by Category"
    valueBox(pom,napis, color = "blue")
  })
  output$vbox81 <- renderValueBox({
    pom <- googleplaystore[[1]][order(googleplaystore[,4], decreasing = TRUE)[1]]
    napis = "Best Rating App"
    valueBox(pom,napis, color = "purple")
  })
  output$vbox82 <- renderValueBox({
    pom <- googleplaystore[[1]][order(googleplaystore[,6], decreasing = TRUE)[1]]
    napis = "Best Popular App"
    valueBox(pom,napis, color = "red")
  })
  
  
}
################################################################################
################################################################################
##############################     SHINY APP     ###############################
################################################################################
################################################################################
shinyApp(ui, server)