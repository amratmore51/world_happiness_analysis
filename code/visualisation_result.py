import pandas as pd
import numpy as np

def visualisation_result_ladder_score(df):
    ladder_score_from_2006_to_2020 = df.iloc[0:15, 2].values
    ladder_score_of_2021 = df.iloc[15, 2]

    print(ladder_score_from_2006_to_2020)
    print(ladder_score_of_2021)

    mean_ladder_score_from_2006_to_2020 = np.mean(
        ladder_score_from_2006_to_2020)
    print('Mean of Ladder Score from 2006 to 2020: ',
          mean_ladder_score_from_2006_to_2020)
    print('Current Ladder Score (2021) : ', ladder_score_of_2021)

    str1 = 'Mean of Ladder Score from 2006 to 2020: ' + '{:.2f}'.format(mean_ladder_score_from_2006_to_2020)
    str2 = 'Current Ladder Score (2021) : ' + str(ladder_score_of_2021)

    if(ladder_score_of_2021 < mean_ladder_score_from_2006_to_2020):
        difference = mean_ladder_score_from_2006_to_2020-ladder_score_of_2021
        print('In 2021 India\' Ladder Score is reduced by %.2f' % difference)
        print('Because Ladder Score of 2021 is less than the MEAN Ladder Score from 2006 to 2020')
        str3 = 'In 2021 India\' Ladder Score is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Ladder Score of 2021 is less than the MEAN Ladder Score from 2006 to 2020'
    elif(ladder_score_of_2021 > mean_ladder_score_from_2006_to_2020):
        difference = ladder_score_of_2021 - mean_ladder_score_from_2006_to_2020
        print("In 2021 India's Ladder Score is improved by %.2f" % difference)
        print('Because Ladder Score of 2021 is more than the MEAN Ladder Score from 2006 to 2020')
        str3 = 'In 2021 India\'s Ladder Score is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Ladder Score of 2021 is more than the MEAN Ladder Score from 2006 to 2020'
    else:
        print("In 2021, India's Ladder Score has not been changed drastically.")
        print('Because Ladder Score of 2021 is EQUAL to the MEAN Ladder Score from 2006 to 2020')
        str3 = "In 2021, India's Ladder Score has not been changed drastically."
        str4 = 'Because Ladder Score of 2021 is EQUAL to the MEAN Ladder Score from 2006 to 2020'

    return str1, str2, str3, str4


def visualisation_result_log_GDP_per_capita(df):
    values_from_2006_to_2020 = df.iloc[0:15, 3].values
    value_of_2021 = df.iloc[15, 3]

    print(values_from_2006_to_2020)
    print(value_of_2021)

    mean_of_2006_to_2020 = np.mean(values_from_2006_to_2020)
    print('Mean of Log GDP per Capita from 2006 to 2020: ', mean_of_2006_to_2020)
    print('Current Log GDP per Capita (2021) : ', value_of_2021)

    str1 = 'Mean of Log GDP per Capita from 2006 to 2020: ' + '{:.2f}'.format(mean_of_2006_to_2020)
    str2 = 'Current Log GDP per Capita (2021) : ' + str(value_of_2021)

    if(value_of_2021 < mean_of_2006_to_2020):
        difference = mean_of_2006_to_2020 - value_of_2021
        print('In 2021 India\' Log GDP per Capita is reduced by %.2f' % difference)
        print('Because Log GDP per Capita of 2021 is less than the MEAN Log GDP per Capita from 2006 to 2020')
        str3 = 'In 2021 India\' Log GDP per Capita is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Log GDP per Capita of 2021 is less than the MEAN Log GDP per Capita from 2006 to 2020'
    elif(value_of_2021 > mean_of_2006_to_2020):
        difference = value_of_2021 - mean_of_2006_to_2020
        print("In 2021 India's Log GDP per Capita is improved by %.2f" % difference)
        print('Because Log GDP per Capita of 2021 is more than the MEAN Log GDP per Capita from 2006 to 2020')
        str3 = 'In 2021 India\'s Log GDP per Capita is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Log GDP per Capita of 2021 is more than the MEAN Log GDP per Capita from 2006 to 2020'
    else:
        print("In 2021, India's Log GDP per Capita has not been changed drastically.")
        print('Because Log GDP per Capita of 2021 is EQUAL to the MEAN Log GDP per Capita from 2006 to 2020')
        str3 = "In 2021, India's Log GDP per Capita has not been changed drastically."
        str4 = 'Because Log GDP per Capita of 2021 is EQUAL to the MEAN Log GDP per Capita from 2006 to 2020'

    return str1, str2, str3, str4


def visualisation_result_social_support(df):
    values_from_2006_to_2020 = df.iloc[0:15, 4].values
    value_of_2021 = df.iloc[15, 4]

    print(values_from_2006_to_2020)
    print(value_of_2021)

    mean_of_2006_to_2020 = np.mean(values_from_2006_to_2020)
    print('Mean of Social Support from 2006 to 2020: ', mean_of_2006_to_2020)
    print('Current Social Support (2021) : ', value_of_2021)

    str1 = 'Mean of Social Support from 2006 to 2020: ' + '{:.2f}'.format(mean_of_2006_to_2020)
    str2 = 'Current Social Support (2021) : ' + str(value_of_2021)

    if(value_of_2021 < mean_of_2006_to_2020):
        difference = mean_of_2006_to_2020 - value_of_2021
        print('In 2021 India\' Social Support is reduced by %.2f' % difference)
        print('Because Social Support of 2021 is less than the MEAN Social Support from 2006 to 2020')
        str3 = 'In 2021 India\' Social Support is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Social Support of 2021 is less than the MEAN Social Support from 2006 to 2020'
    elif(value_of_2021 > mean_of_2006_to_2020):
        difference = value_of_2021 - mean_of_2006_to_2020
        print("In 2021 India's Social Support is improved by %.2f" % difference)
        print('Because Social Support of 2021 is more than the MEAN Social Support from 2006 to 2020')
        str3 = 'In 2021 India\'s Social Support is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Social Support of 2021 is more than the MEAN Social Support from 2006 to 2020'
    else:
        print("In 2021, India's Social Support has not been changed drastically.")
        print('Because Social Support of 2021 is EQUAL to the MEAN Social Support from 2006 to 2020')
        str3 = "In 2021, India's Social Support has not been changed drastically."
        str4 = 'Because Social Support of 2021 is EQUAL to the MEAN Social Support from 2006 to 2020'

    return str1, str2, str3, str4

def visualisation_result_healthy_life_expectancy(df):
    values_from_2006_to_2020 = df.iloc[0:15, 5].values
    value_of_2021 = df.iloc[15, 5]

    print(values_from_2006_to_2020)
    print(value_of_2021)

    mean_of_2006_to_2020 = np.mean(values_from_2006_to_2020)
    print('Mean of Healthy Life Expectancy from 2006 to 2020: ', mean_of_2006_to_2020)
    print('Current Healthy Life Expectancy (2021) : ', value_of_2021)

    str1 = 'Mean of Healthy Life Expectancy from 2006 to 2020: ' + '{:.2f}'.format(mean_of_2006_to_2020)
    str2 = 'Current Healthy Life Expectancy (2021) : ' + str(value_of_2021)

    if(value_of_2021 < mean_of_2006_to_2020):
        difference = mean_of_2006_to_2020 - value_of_2021
        print('In 2021 India\' Healthy Life Expectancy is reduced by %.2f' % difference)
        print('Because Healthy Life Expectancy of 2021 is less than the MEAN Healthy Life Expectancy from 2006 to 2020')
        str3 = 'In 2021 India\' Healthy Life Expectancy is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Healthy Life Expectancy of 2021 is less than the MEAN Healthy Life Expectancy from 2006 to 2020'
    elif(value_of_2021 > mean_of_2006_to_2020):
        difference = value_of_2021 - mean_of_2006_to_2020
        print("In 2021 India's Healthy Life Expectancy is improved by %.2f" % difference)
        print('Because Healthy Life Expectancy of 2021 is more than the MEAN Healthy Life Expectancy from 2006 to 2020')
        str3 = 'In 2021 India\'s Healthy Life Expectancy is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Healthy Life Expectancy of 2021 is more than the MEAN Healthy Life Expectancy from 2006 to 2020'
    else:
        print("In 2021, India's Healthy Life Expectancy has not been changed drastically.")
        print('Because Healthy Life Expectancy of 2021 is EQUAL to the MEAN Healthy Life Expectancy from 2006 to 2020')
        str3 = "In 2021, India's Healthy Life Expectancy has not been changed drastically."
        str4 = 'Because Healthy Life Expectancy of 2021 is EQUAL to the MEAN Healthy Life Expectancy from 2006 to 2020'

    return str1, str2, str3, str4

def visualisation_result_freedom_to_make_life_choice(df):
    values_from_2006_to_2020 = df.iloc[0:15, 6].values
    value_of_2021 = df.iloc[15, 6]

    print(values_from_2006_to_2020)
    print(value_of_2021)

    mean_of_2006_to_2020 = np.mean(values_from_2006_to_2020)
    print('Mean of Freedom to Make Life Choices from 2006 to 2020: ', mean_of_2006_to_2020)
    print('Current Freedom to Make Life Choices (2021) : ', value_of_2021)

    str1 = 'Mean of Freedom to Make Life Choices from 2006 to 2020: ' + '{:.2f}'.format(mean_of_2006_to_2020)
    str2 = 'Current Freedom to Make Life Choices (2021) : ' + str(value_of_2021)

    if(value_of_2021 < mean_of_2006_to_2020):
        difference = mean_of_2006_to_2020 - value_of_2021
        print('In 2021 India\' Freedom to Make Life Choices is reduced by %.2f' % difference)
        print('Because Freedom to Make Life Choices of 2021 is less than the MEAN Freedom to Make Life Choices from 2006 to 2020')
        str3 = 'In 2021 India\' Freedom to Make Life Choices is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Freedom to Make Life Choices of 2021 is less than the MEAN Freedom to Make Life Choices from 2006 to 2020'
    elif(value_of_2021 > mean_of_2006_to_2020):
        difference = value_of_2021 - mean_of_2006_to_2020
        print("In 2021 India's Freedom to Make Life Choices is improved by %.2f" % difference)
        print('Because Freedom to Make Life Choices of 2021 is more than the MEAN Freedom to Make Life Choices from 2006 to 2020')
        str3 = 'In 2021 India\'s Freedom to Make Life Choices is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Freedom to Make Life Choices of 2021 is more than the MEAN Freedom to Make Life Choices from 2006 to 2020'
    else:
        print("In 2021, India's Freedom to Make Life Choices has not been changed drastically.")
        print('Because Freedom to Make Life Choices of 2021 is EQUAL to the MEAN Freedom to Make Life Choices from 2006 to 2020')
        str3 = "In 2021, India's Freedom to Make Life Choices has not been changed drastically."
        str4 = 'Because Freedom to Make Life Choices of 2021 is EQUAL to the MEAN Freedom to Make Life Choices from 2006 to 2020'

    return str1, str2, str3, str4

def visualisation_result_generosity(df):
    values_from_2006_to_2020 = df.iloc[0:15, 7].values
    value_of_2021 = df.iloc[15, 7]

    print(values_from_2006_to_2020)
    print(value_of_2021)

    mean_of_2006_to_2020 = np.mean(values_from_2006_to_2020)
    print('Mean of Generosity from 2006 to 2020: ', mean_of_2006_to_2020)
    print('Current Generosity (2021) : ', value_of_2021)

    str1 = 'Mean of Generosity from 2006 to 2020: ' + '{:.2f}'.format(mean_of_2006_to_2020)
    str2 = 'Current Generosity (2021) : ' + str(value_of_2021)

    if(value_of_2021 < mean_of_2006_to_2020):
        difference = mean_of_2006_to_2020 - value_of_2021
        print('In 2021 India\' Generosity is reduced by %.2f' % difference)
        print('Because Generosity of 2021 is less than the MEAN Generosity from 2006 to 2020')
        str3 = 'In 2021 India\' Generosity is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Generosity of 2021 is less than the MEAN Generosity from 2006 to 2020'
    elif(value_of_2021 > mean_of_2006_to_2020):
        difference = value_of_2021 - mean_of_2006_to_2020
        print("In 2021 India's Generosity is improved by %.2f" % difference)
        print('Because Generosity of 2021 is more than the MEAN Generosity from 2006 to 2020')
        str3 = 'In 2021 India\'s Generosity is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Generosity of 2021 is more than the MEAN Generosity from 2006 to 2020'
    else:
        print("In 2021, India's Generosity has not been changed drastically.")
        print('Because Generosity of 2021 is EQUAL to the MEAN Generosity from 2006 to 2020')
        str3 = "In 2021, India's Generosity has not been changed drastically."
        str4 = 'Because Generosity of 2021 is EQUAL to the MEAN Generosity from 2006 to 2020'

    return str1, str2, str3, str4


def visualisation_perceptions_of_corruptions(df):
    values_from_2006_to_2020 = df.iloc[0:15, 8].values
    value_of_2021 = df.iloc[15, 8]

    print(values_from_2006_to_2020)
    print(value_of_2021)

    mean_of_2006_to_2020 = np.mean(values_from_2006_to_2020)
    print('Mean of Perceptions of Corruption from 2006 to 2020: ', mean_of_2006_to_2020)
    print('Current Perceptions of Corruption (2021) : ', value_of_2021)

    str1 = 'Mean of Perceptions of Corruption from 2006 to 2020: ' + '{:.2f}'.format(mean_of_2006_to_2020)
    str2 = 'Current Perceptions of Corruption (2021) : ' + str(value_of_2021)

    if(value_of_2021 < mean_of_2006_to_2020):
        difference = mean_of_2006_to_2020 - value_of_2021
        print('In 2021 India\' Perceptions of Corruption is reduced by %.2f' % difference)
        print('Because Perceptions of Corruption of 2021 is less than the MEAN Perceptions of Corruption from 2006 to 2020')
        str3 = 'In 2021 India\' Perceptions of Corruption is reduced by {:.2f}'.format(
            difference)
        str4 = 'Because Perceptions of Corruption of 2021 is less than the MEAN Perceptions of Corruption from 2006 to 2020'
    elif(value_of_2021 > mean_of_2006_to_2020):
        difference = value_of_2021 - mean_of_2006_to_2020
        print("In 2021 India's Perceptions of Corruption is improved by %.2f" % difference)
        print('Because Perceptions of Corruption of 2021 is more than the MEAN Perceptions of Corruption from 2006 to 2020')
        str3 = 'In 2021 India\'s Perceptions of Corruption is improved by {:.2f}'.format(
            difference)
        str4 = 'Because Perceptions of Corruption of 2021 is more than the MEAN Perceptions of Corruption from 2006 to 2020'
    else:
        print("In 2021, India's Perceptions of Corruption has not been changed drastically.")
        print('Because Perceptions of Corruption of 2021 is EQUAL to the MEAN Perceptions of Corruption from 2006 to 2020')
        str3 = "In 2021, India's Perceptions of Corruption has not been changed drastically."
        str4 = 'Because Perceptions of Corruption of 2021 is EQUAL to the MEAN Perceptions of Corruption from 2006 to 2020'

    return str1, str2, str3, str4
