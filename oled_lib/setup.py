from distutils.core import setup, Extension

def main():
    setup(name="dd_oled_lib",
        version='1.0.0',
        description="Python Interface for OLED display functions",
        author="Bassam Ali & Yousef Ali",
        author_email="bassam2.ali@live.uwe.ac.uk",
        ext_modules=[Extension("dd_oled",["dd_oled.c","oled.c","fonts.c"])]
        )
    
if __name__ == "__main__":
    main()
