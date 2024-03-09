import streamlit as st

# set the title, header, subheader, text tag
st.title("Title : Hi Manohar, Welcome to my Webpage")             #title
st.header("Header : Hi this is header")                           #header
st.subheader("SubHeader : Hi this is subheader")                  #subheader
st.text("Text : This is text")                                    #text


st.markdown("# Hi")                                               #markdown
st.markdown("## Hii")
st.markdown("### Hi")
st.markdown("#### Hi")
st.markdown("##### Hi")

# to display a succeess msg/notific
st.success("Data is Submitted!")                                  #success  
st.info("Information!")                                           #info(ideally blue color)
st.warning("Warning!")                                            #warning
st.error("Error!")                                                #error

#to disply error specifically Exception Handling
st.exception(ZeroDivisionError("Division not possible with Zero"))

st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
# st.text(1+2)
st.write(1+2)   


st.code('x = 10\n''for i in range(1,10)\n''\tprint(x)')


# Checkbox in streamlit------------------------------------------------------------------------------
st.subheader("Checkbox")
st.checkbox("Female")

if(st.checkbox("Male")):
    st.write("You are a Male")


# Radio box in streamlit---------------------------------------------
st.subheader("RadioBox")

radiobox = st.radio("select :", ('NSS',"NCC"))

if(radiobox == "NCC"):
    st.write("You are an NCC cadet, Congratuations!!")

if(radiobox == "NSS"):
    st.write("You are an NSS cadet, Congratuations!!")

# Select box -------------------------------------------------------
st.subheader("SelectBox")

sbox = st.selectbox("Data Science :",["None","Deep Learning","Machine Learning", "Web Scraping","Data Analysis"])

if sbox !="None":
    st.write("You have Selected:",sbox)
    
# Multi Select Box------------------------------------------------------------------------------

st.subheader("MultiSelectBox")
multibox = st.multiselect("Data Science :",["None","Deep Learning","Machine Learning", "Web Scraping","Data Analysis"])

st.write("You have selected : ",len(multibox),"Courses")


#Button ------------------------------------------------------------------------------

st.subheader("Buttons")
if(st.button("Click on me")):
    st.write("Thanks for clicking on me")
    
    
# Slider -------------------------------------------------------------------------------------------------
st.subheader("Slider")

choice = st.slider("Select the Temperature:",0,100, step = 5)
st.write("You have selected",choice,"Temperature for your Air Conditioner")

# User Input------------------------------------------------------------------------------
st.subheader("User Input")
username = st.text_input("Username:")
password = st.text_input("Password:",type = 'password')

# Text area for large input ------------------------------------------------------------------------------
st.subheader("Text Area")

textArea = st.text_area("Write an interesting story in 500 words", height = 20)#height will be fixed
# a scroll bar appears inside   
st.write(textArea)

# Number, date, age input------------------------------------------------------------------------------
st.subheader("Input Number")
st.number_input("Enter your age:",3,60)

st.subheader("Input your Date of Birth")
st.date_input("DOB:")

st.subheader("Input Time")
st.time_input("Time:")








