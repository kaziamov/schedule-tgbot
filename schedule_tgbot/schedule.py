schedule_data = {
        "карате": {"вторник": ['17:30', "19:00"],
                   "понедельник": ['17:30', "19:00"],
                   },
        "марате": {"понедельник": ['17:30', "19:00"],
                   "понедельник": ['17:30', "19:00"],
                   },
        "бурате": {"вторник": ['17:30', "19:00"],
                   "пятница": ['17:30', "19:00"],
                   },
        "квадрате": {"вторник": ['17:30', "19:00"],
                   "среда": ['17:30', "19:00"],
                     }
}


def get_sections():
    return list(schedule_data.keys())


async def schedule_for_day(day):
    """Parse and return all sections in selected day"""
    result = []
    async for section in schedule_data:
        if schedule_data[section].get(day, False):
            async for d in section[day]:
                await result.append(f"{section.capitalize()} - {d}")
    return await "\n".join(result)


async def schedule_for_section(section):
    """Parse and return schedule time in week for selected section"""
    result = []
    if schedule_data.get(section, False):
        async for key, value in schedule_data[section].items():
            async for time in value:
                await result.append(f"{key} - {time}")
    return await "\n".join(result)


message = """Multi
line
string"""

if __name__ == "__main__":
    print(message)
