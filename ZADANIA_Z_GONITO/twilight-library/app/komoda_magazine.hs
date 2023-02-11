
{-# LANGUAGE Arrows, NoMonomorphismRestriction #-}
import ShadowLibrary.Core

import Text.XML.HXT.Core
import Text.XML.HXT.XPath
import Text.XML.HXT.Curl
import Data.List
import Data.List.Utils (replace)

import Text.Regex.Posix
import Text.Printf
import Network.HTTP


xMonthNameToNumber :: String -> String
xMonthNameToNumber "January"     = "01"
xMonthNameToNumber "February"    = "02"
xMonthNameToNumber "March"       = "03"
xMonthNameToNumber "April"       = "04"
xMonthNameToNumber "May"         = "05"
xMonthNameToNumber "June"        = "06"
xMonthNameToNumber "July"        = "07"
xMonthNameToNumber "August"      = "08"
xMonthNameToNumber "September"   = "09"
xMonthNameToNumber "October"     = "10"
xMonthNameToNumber "November"    = "11"
xMonthNameToNumber "December"    = "12"


extractRecords = extractLinksWithText "//a[contains(@title, '(Pol)')]"
                 >>> second (arr $ replace "  " "")
                 >>> second (arr $ replace " \n" "")
                 >>> second (arr $ replace "\n " "")
                 >>> second (arr $ replace "\n" "")
                 >>> first (extractLinksWithText "//a[contains(@class,'format') and contains(@href, 'Pol.pdf')]")

toShadowItem :: ((String, String), String) -> ShadowItem
toShadowItem ((url, pom), yearlyTitle) =
  (defaultShadowItem url title) {
    originalDate = Just date,
    itype = "periodical",
    format = Just "pdf",
    finalUrl = url
    }
  where title = getTitle yearlyTitle
        date = getDate yearlyTitle

getDate yearlyTitle =
  case yearlyTitle =~~ "([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]{3,}) (19[0-9][0-9]|20[0-9][0-9])" :: Maybe [[String]] of
    Just [[_, month, year]] ->  year ++ "-" ++ xMonthNameToNumber  month
    otherwise -> getDate2 yearlyTitle

getDate2 yearlyTitle =
  case yearlyTitle =~~ "(19[0-9][0-9]|20[0-9][0-9])" :: Maybe [[String]] of
    Just [[_, year]] ->  year
    otherwise -> yearlyTitle

getTitle url =
  case url =~~ "(Komoda [0-9][0-9] )\\(([a-zA-Z]* [0-9]*)" :: Maybe [[String]] of
    Just [[_, title, monthANDyear]] ->  title ++ monthANDyear
    otherwise -> getTitle2 url

getTitle2 url =
  case url =~~ "(Komoda [0-9][0-9] )\\((19[0-9][0-9]|20[0-9][0-9])" :: Maybe [[String]] of
    Just [[_, title, year]] ->  title ++ year
    otherwise -> url

main = do
    let start = "https://archive.org/details/komoda_magazine"
       
    let shadowLibrary = ShadowLibrary {logoUrl=Nothing,
                                       lname="Czasopismo Komoda",
                                       abbrev="Komoda",
                                       lLevel=0,
                                       webpage=start}
    extractItemsStartingFromUrl shadowLibrary start (extractRecords >>> arr toShadowItem)
