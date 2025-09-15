from datetime import datetime 
from zoneinfo import ZoneInfo, available_timezones

INDY = 'America/Indianapolis'
NYC = 'America/New_York'
VANCOUVER = 'America/Vancouver'
ADELAIDE = 'Australia/Adelaide'
MELBOURNE = 'Australia/Melbourne'
TELL_CITY = 'America/Indiana/Tell_City'
MONTREAL = 'America/Montreal'

ZONES_INFO = (
    NYC,
    INDY,
    TELL_CITY,
    MONTREAL,
    VANCOUVER,
    MELBOURNE,
    ADELAIDE,
)

APP_ZONES = [
        "Indianapolis",
        "Montreal",
        "NYC",
        "Adelaide",
        "Melbourne",
        "Vancouver",
        "Tell City"
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

    play.update({"day": getDay()})
    play.update({"hour": getHour()})
    play.update({"minute": getMinute()})
    
    return play
    

def getDay():
    """Get day from user."""
    msg = "Enter day of month to play: "
    day = input(msg)
    return int(day)


def getHour():
    """Get Hour from user."""
    msg = "Enter hour of day to play: "
    hour = input(msg)
    return int(hour)


def getMinute():
    """Get minute from user."""
    msg = "Enter minute of hour, if any. If none press Enter: "
    minute = input(msg)
    if not minute:
        minute = 0
    else:
        minute = int(minute)
    return minute


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


def getZones(zoneList: list[str], dateObj: datetime, zoneDict: dict) -> dict:
    """Return a dictionary holding the results of the required time zone translation."""
    results = {}
    for zone in zoneList:
        results.update({zone: timeZone(dateObj, zoneDict[zone])})

    return results

# Run the script
if __name__ == "__main__":
    main()
