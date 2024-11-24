def get_slides_files(slides_folder='/Users/francis/Documents/Courses/7607 NLP/Project/OS-Copilot-main/working_dir/Slides'):
    """
    Retrieve the list of files from the specified 'Slides' folder.
    Args:
        slides_folder (str): Full path to the Slides folder. 
            Defaults to the standard location in the working directory.
    Returns:
        list: A list of file names present in the Slides folder.
    """
    import os
    # Check if the folder exists
    if not os.path.exists(slides_folder):
        raise FileNotFoundError(f"The Slides folder does not exist at {slides_folder}")
    # Get list of all files in the folder
    files = [f for f in os.listdir(slides_folder) if os.path.isfile(os.path.join(slides_folder, f))]
    return files