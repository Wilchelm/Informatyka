
{-# LANGUAGE Arrows, NoMonomorphismRestriction #-}
import ShadowLibrary.Core

import Text.XML.HXT.Core
import Text.XML.HXT.XPath
-- import Text.XML.HXT.Curl
import Data.List
import Data.List.Utils (replace)

import Text.Regex.Posix
import Text.Printf

xMonthNameToNumber :: String -> String
xMonthNameToNumber "Styczeń"     = "01"
xMonthNameToNumber "Luty"        = "02"
xMonthNameToNumber "Marzec"      = "03"
xMonthNameToNumber "Kwiecień"    = "04"
xMonthNameToNumber "Maj"         = "05"
xMonthNameToNumber "Czerwiec"    = "06"
xMonthNameToNumber "Lipiec"      = "07"
xMonthNameToNumber "Sierpień"    = "08"
xMonthNameToNumber "Wrzesień"    = "09"
xMonthNameToNumber "Październik" = "10"
xMonthNameToNumber "Listopad"    = "11"
xMonthNameToNumber "Grudzień"    = "12"
xMonthNameToNumber "styczeń"     = "01"
xMonthNameToNumber "styczen"     = "01"
xMonthNameToNumber "stycznia"     = "01"
xMonthNameToNumber "luty"        = "02"
xMonthNameToNumber "lutego"        = "02"
xMonthNameToNumber "marzec"      = "03"
xMonthNameToNumber "marca"      = "03"
xMonthNameToNumber "kwiecień"    = "04"
xMonthNameToNumber "kwiecien"    = "04"
xMonthNameToNumber "kwietnia"    = "04"
xMonthNameToNumber "maj"         = "05"
xMonthNameToNumber "maja"         = "05"
xMonthNameToNumber "czerwiec"    = "06"
xMonthNameToNumber "czeerwiec"    = "06"
xMonthNameToNumber "czerwca"    = "06"
xMonthNameToNumber "lipiec"      = "07"
xMonthNameToNumber "lipca"      = "07"
xMonthNameToNumber "sierpień"    = "08"
xMonthNameToNumber "sierpien"    = "08"
xMonthNameToNumber "sierpnia"    = "08"
xMonthNameToNumber "wrzesień"    = "09"
xMonthNameToNumber "wrzesien"    = "09"
xMonthNameToNumber "września"    = "09"
xMonthNameToNumber "wrzesnia"    = "09"
xMonthNameToNumber "październik" = "10"
xMonthNameToNumber "pażdziernik" = "10"
xMonthNameToNumber "pazdziernik" = "10"
xMonthNameToNumber "października" = "10"
xMonthNameToNumber "pazdziernika" = "10"
xMonthNameToNumber "listopad"    = "11"
xMonthNameToNumber "listopada"    = "11"
xMonthNameToNumber "grudzień"    = "12"
xMonthNameToNumber "grudzien"    = "12"
xMonthNameToNumber "grudnia"    = "12"
xMonthNameToNumber "jesien"    = "10"

myExtract  = downloadDocument
             >>> getXPathTrees "//div[@class='so-widget-sow-editor so-widget-sow-editor-base']"
             >>> ((getXPathTrees "//h3[@class='widget-title']" >>> extractText)
                  &&&
                  (getXPathTrees "//p/a[contains(@href,'.pdf') and img]" >>> getAttrValue "href"))

extractRecords = myExtract

toShadowItem :: (String, String) -> ShadowItem
toShadowItem (yearlyTitle, url) =
  (defaultShadowItem url title) {
    originalDate = Just date,
    itype = "periodical",
    format = Just "pdf",
    finalUrl = url
    }
  where title = "Wiadomości Wiśnickie " ++ yearlyTitle
        date = getDate yearlyTitle

getDate yearlyTitle =
  case yearlyTitle =~~ "([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]{3,}) (19[0-9][0-9]|20[0-9][0-9])" :: Maybe [[String]] of
    Just [[_, month, year]] ->  year ++ "-" ++ xMonthNameToNumber  month
    otherwise -> yearlyTitle

main = do
    let start = "http://tmw.iaw.pl/wiadomosci-wisnickie/"
    let shadowLibrary = ShadowLibrary {logoUrl=Nothing,
                                       lname="Wiadomości Wiśnickie",
                                       abbrev="WiadWisn",
                                       lLevel=0,
                                       webpage=start}
    extractItemsStartingFromUrl shadowLibrary start (extractRecords >>> arr toShadowItem)
