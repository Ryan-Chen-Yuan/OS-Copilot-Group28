# Event to Calandar

## Command line Example

default(text):

```bash
python event_to_calendar.py
```

text-based event:

```bash
python event_to_calendar.py --query "Dec 11 WED 6:30 pm - 8:30 pm COMP7107 Management of complex data types Venue: CPD-LG.07-10, Centennial Campus"
```

image-based event:

```bash
python event_to_calendar.py --query_file_path "./working_dir/images/screenshot1.jpg"
```

## Tools Setup

```bash
python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name format_datetime_objects --tool_path oscopilot/tool_repository/basic_tools/format_datetime_objects.py

python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name parse_string_to_datetime_objects --tool_path oscopilot/tool_repository/basic_tools/parse_string_to_datetime_objects.py
```

## Output

``` txt
└── output
    ├── image_event_example_output.jpg
    ├── image_event_example_procedure.txt
    ├── text_event_example_output.jpg
    └── text_event_example_procedure.txt
```
