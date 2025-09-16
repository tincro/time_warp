from datetime import datetime 
from zoneinfo import ZoneInfo, available_timezones

INDY = 'America/Indianapolis'
NYC = 'America/New_York'
VANCOUVER = 'America/Vancouver'
ADELAIDE = 'Australia/Adelaide'
MELBOURNE = 'Australia/Melbourne'
MONTREAL = 'America/Montreal'
CHICAGO = 'America/Chicago'

ZONES_INFO = (
    NYC,
    INDY,
    CHICAGO,
    MONTREAL,
    VANCOUVER,
    MELBOURNE,
    ADELAIDE,
)

APP_ZONES = [
        "Indianapolis",
        "Chicago",
        "Montreal",
        "NYC",
        "Adelaide",
        "Melbourne",
        "Vancouver"
    ]

FORMAT = "%a %X %p %Z"


def main():
    # Dictionary to hold zones info
    zones = zoneBuilder(ZONES_INFO)

    # Gather user input
    time_to_play = getTimeToPlay()
    date_to_play = getDate(time_to_play)

    printList = ["Montreal", "Vancouver", "Adelaide"]
    
    # Print to user
    printZones(printList, date_to_play, zones)


# Helper methods
def searchTimeZone(zoneStr):
    """Helper method to search library for time zones data."""
    for zone in available_timezones():
        if zoneStr in zone:
            print(zone)      


def zoneBuilder(list) -> dict:
    """Build ZoneInfo objects from list"""
    zones = {}
    for loc in list:
        zones.update({parseLocation(loc): ZoneInfo(loc)})

    return zones


def parseLocation(zone):
    """Helper method to get location from timezones"""
    location_list = zone.split('/')
    loc = location_list[-1]
    
    if "_" in loc:
        loc = loc.replace("_", " ")
    
    return loc
    

# Main methods
def getTimeToPlay():
    """Get user input on time to play"""
    print("What day are we playing?: -->")
    play = {}

    play.update({"day": getDayFromUser()})
    play.update({"hour": getHourFromUser()})
    play.update({"minute": getMinuteFromUser()})
    
    return play
    

def getDayFromUser():
    """Get day from user."""
    msg = "Enter day of month to play: "
    day = input(msg)
    return int(day)


def getHourFromUser():
    """Get Hour from user."""
    msg = "Enter hour of day to play: "
    hour = input(msg)
    return int(hour)


def getMinuteFromUser():
    """Get minute from user."""
    msg = "Enter minute of hour, if any. If none press Enter: "
    minute = input(msg)
    if not minute:
        minute = 0
    else:
        minute = int(minute)
    return minute


def getDateFromStr(dateStr) -> dict:
    """return date dict from given stting."""
    date_dict = {}
    if dateStr is None:
        return date_dict
    
    try:
        date = datetime.fromisoformat(dateStr)
        date_dict.update({'day': date.day, 'month': date.month, 'year': date.year})
    except:
        print("Missing date format.")
    return date_dict


def getYearFromStr(dateStr) -> int|None:
    """Return day substring from given string."""
    try:
        date = datetime.fromisoformat(dateStr)
        return date.year
    except:
        print("Not supported date string format.")


def getMonthFromStr(dateStr) -> int|None:
    """Return day substring from given string."""
    try:
        date = datetime.fromisoformat(dateStr)
        return date.month
    except:
        print("Not supported date string format.")


def getDayFromStr(dateStr) -> int|None:
    """Return day substring from given string."""
    try:
        date = datetime.fromisoformat(dateStr)
        return date.day
    except:
        print("Not supported date string format.")


def getTimeFromStr(timeStr) -> dict:
    """Return dictionary of time from given string."""
    time_dict = {}

    if timeStr is None:
        return time_dict
    

    time = timeStr.split(":")
    try:
        time_dict.update({'hour': int(time[0]), 'minute': int(time[1])})
    except:
        print("Missing format on time string.")

    return time_dict



def getDate(info: dict) -> datetime:
    "Return a new date object from info."
    day = info.get("day")
    hour = info.get("hour")
    minute = info.get("minute")

    return newDate(day, hour, minute)


def newDate(day, hour, minute, year=None, month=None) -> datetime:
    """Return new DeltaTime for date to play"""
    year = datetime.now().year if year == None else year
    month = datetime.now().month if month == None else month
    try:
        return datetime(year, month, day, hour, minute)
    except ValueError as e:
        print(e, "Please try again.")
        return datetime(0,0,0)


def timeZone(date: datetime, timezone: ZoneInfo) -> str:
    """Return time zone displayed as input."""

    try:
        return date.astimezone(timezone).strftime(FORMAT)
    except(AttributeError) as e:
        print("Invalid formatting in date/time input.")
        return ""


def printZones(zoneList: list[str], dateObj: datetime, zoneDict: dict):
    """Print the zone in the list."""
    for item in zoneList:
        zoneStr = timeZone(dateObj, zoneDict[item])
        if zoneStr is None:
            print("No valid zone information to display.")
            return
        # check if item is approved
        if item in APP_ZONES:
            try:
                
                print(f"{str(item).upper()}:", zoneStr)
            except KeyError:
                print("No Time Zone Info Found.")


def getZones(zoneList: list[str], dateObj: datetime) -> dict:
    """Return a dictionary holding the results of the required time zone translation."""
    zones = zoneBuilder(ZONES_INFO)
    results = {}
    for zone in zoneList:
        results.update({zone: timeZone(dateObj, zones[zone])})

    return results

# Run the script
if __name__ == "__main__":
    main()
