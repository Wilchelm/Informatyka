/** @OnlyCurrentDoc */
//lorem ipsum


function green() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Uzytkownik+sesja) - dopasowania'), true);
  spreadsheet.getRange('G3').activate();
  spreadsheet.getRange('G4:U4').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  history();
  spreadsheet.getRange('L9').setValue('green');
  nodups();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)'), true);
};

function red() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Uzytkownik+sesja) - dopasowania'), true);
  spreadsheet.getRange('G3').activate();
  spreadsheet.getRange('G5:U5').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  history();
  spreadsheet.getRange('L9').setValue('red');
  nodups();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)'), true);
};


//zwraca "Service error: Spreadsheets" gdy są złe zakresy
function history() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)'), true);
  //Przesuń historię o 1 w dół
  spreadsheet.getRange('L10').activate(); //??
  spreadsheet.getRange('L9:Q41').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false); //??
  //Dodaj nowy element do historii
  spreadsheet.getRange('M9').activate();
  spreadsheet.getRange('A10:E10').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
};

function nodups(){
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)'), true);
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();
  //var koor = spreadsheet.getRange('C12');
  var koordynaty = spreadsheet.getRange('(Interfejs + Logi uzytkownika)!C12').getValue();
  //spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Uzytkownik+sesja) - dopasowania'), true);
  var sheet = ss.getSheetByName('(Uzytkownik+sesja) - dopasowania');
  sheet.getRange(koordynaty,2).setValue('x');
};

function restart() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)'), true);
  //Usuwanie historii
  spreadsheet.getRange('L9:Q').activate();
  spreadsheet.getSelection().getNextDataRange(SpreadsheetApp.Direction.DOWN).activate();
  spreadsheet.getActiveRangeList().clear({contentsOnly: true, skipFilteredRows: true});
  //Reset wag
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Uzytkownik+sesja) - dopasowania'), true);
  spreadsheet.getRange('G3').activate();
  spreadsheet.getRange('G2:U2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_NORMAL, false);
  //Reset duplikatów 
  spreadsheet.getRange('B12:B').activate();
  var currentCell = spreadsheet.getCurrentCell();
  spreadsheet.getSelection().getNextDataRange(SpreadsheetApp.Direction.DOWN).activate();
  spreadsheet.getActiveRangeList().clear({contentsOnly: true, skipFilteredRows: true});
  //Powrót na interfejs
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)'), true);
};


function newuser() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Uzytkownicy'), true);
  spreadsheet.getRange('A1').activate();
  spreadsheet.getCurrentCell().getNextDataCell(SpreadsheetApp.Direction.DOWN).activate();
  //przesuń kursor o jedno miejsce w dół
  var cursor = spreadsheet.getActiveCell();
  var range = cursor.offset(1,0)
  spreadsheet.setActiveRange(range);
  //wklej nową parę Nazwa Uzytkownika - Klucz Uzytkownika
  spreadsheet.getRange('G1:H1').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  var cursor = spreadsheet.getActiveCell();
  
  var dataArray = []
  var record ={};
  
  record['user'] = cursor.getValue();
  
  //przesuń kursor o jedno miejsce w prawo
  var range = cursor.offset(0,1);
  spreadsheet.setActiveRange(range);
  var cursor = spreadsheet.getActiveCell();
  
  record['hash-pass'] = cursor.getValue();
  
  
  dataArray.push(record)
  var json = {};

  json.item=dataArray;
  var result = JSON.stringify(json)
  return ContentService.createTextOutput(result).setMimeType(ContentService.MimeType.JSON);
};

function doGet(e) {
  var action = e.parameter.action;
  var spreadsheet = SpreadsheetApp.getActive();
  var sheet = spreadsheet.getSheetByName('(Interfejs + Logi uzytkownika)');
  
  if (action=='getItem') {
    return getItem(sheet);
  }
  
    if (action=='evaluate') {
    return evaluate(sheet);
  }
  
  if (action=='green') {
    return green('ok-green');
  }
  
  if (action=='red') {
    return red('ok-red');
  }
  
  if (action=='newuser') {
    return newuser();
  }
};


function getItem(sheet) {
  var jo = {};
  var dataArray = [];
  var d10 = sheet.getRange('D10').getValue();
  var e10 = sheet.getRange('E10').getValue();
  var f10 = sheet.getRange('F10').getValue();
  
  var record = {};
  record['photo'] = d10;
  record['name'] = e10;
  record['description'] = f10;
  
  dataArray.push(record);
  
  jo.item = dataArray;
  var result = JSON.stringify(jo);
  
  return ContentService.createTextOutput(result).setMimeType(ContentService.MimeType.JSON);
  
};

function evaluate(sheet) {
  var jo = {};
  var dataArray = [];
  var d10 = sheet.getRange('W10').getValue();
  var e10 = sheet.getRange('X10').getValue();
  var f10 = sheet.getRange('Y10').getValue();
  
  var record = {};
  record['photo'] = d10;
  record['name'] = e10;
  record['description'] = f10;
  
  dataArray.push(record);
  
  jo.item = dataArray;
  var result = JSON.stringify(jo);
  
  restart();
  
  return ContentService.createTextOutput(result).setMimeType(ContentService.MimeType.JSON);
  
};
