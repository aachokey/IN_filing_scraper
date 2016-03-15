#! python3
# This is a scraper for the 2016 Indiana governor's candidates.
from bs4 import BeautifulSoup
import requests
import csv
import time


# Global variables
contribs_base_url = "http://campaignfinance.in.gov/PublicSite/Filings/Schedules/ViewContributionSchedule.aspx?FilingID="
expenses_base_url = "http://campaignfinance.in.gov/PublicSite/Filings/Schedules/ViewExpenditureSchedule.aspx?FilingID="
contrib_headers = ["date", "type", "contributor", "address", "occupation", "amount", "aggregate", "election_comm", "explanation"]
expense_headers = ["date", "disbursement_type", "expenditure_type", "payee", "address", "occupation", "amount", "explanation"]
pence_filings = [58176, 58175, 54573, 54572, 50042, 50041, 45265, 45264, 45263, 45262, 45261, 44726, 44727]
gregg_filings = [58162, 58161, 54567, 54566, 50028, 50027, 51099, 45245, 45244, 45243, 45242, 45241, 44734]

def main():
    """
    Our function names are a table of contents for what we want to do.
    """
    start_time = time.time()
    get_pence_expenses()
    get_pence_contribs()
    get_gregg_expenses()
    get_gregg_contribs()
    print("All files are scraped. It took " " %s seconds." % (time.time() - start_time))


def get_pence_expenses():
    # Loop through each of the filings for Pence.
    for filing in pence_filings:
        filing_page = expenses_base_url + str(filing)
        r = requests.get(filing_page)
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find('table', attrs={'class': 'frmDataGrid'})
    # Collect all of the rows from the table.
        try:
            list_of_rows = []
            for row in table.findAll('tr'):
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.strip().replace('\n', ' ')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)
    # Write the results to a csv file
            with open("pence/expense-" + str(filing) + ".csv", "w", newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(list_of_rows)
    # Exception in case there aren't any entries for that filing. Be sure to manually check when bulletproofing.
        except:
            print("There might not be a anything here for file " + str(filing) + ".")
            continue
        print("Finished file number %s." % filing)
        time.sleep(3)
    print("Pence's expenditures have been scraped.")


def get_pence_contribs():
    # Loop through each of the filings for Pence.
    for filing in pence_filings:
        filing_page = contribs_base_url + str(filing)
        r = requests.get(filing_page)
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find('table', attrs={'class': 'frmDataGrid'})

    # Collect all of the rows from the table.
        try:
            list_of_rows = []
            for row in table.findAll('tr'):
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.strip().replace('\n', ' ')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)

    # Write the results to a csv file
            with open("pence/contrib-" + str(filing) + ".csv", "w", newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(list_of_rows)
        except:
            print("There might not be a anything here for file " + str(filing) + ".")
            continue
        print("Finished file number %s." % filing)
        time.sleep(3)
    print("Pence's contributions have been scraped.")


def get_gregg_expenses():

    # Loop through each of the filings for Gregg.
    for filing in gregg_filings:
        filing_page = expenses_base_url + str(filing)
        r = requests.get(filing_page)
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find('table', attrs={'class': 'frmDataGrid'})

    # Collect all of the rows from the table.
        try:
            list_of_rows = []
            for row in table.findAll('tr'):
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.strip().replace('\n', ' ')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)

    # Write the results to a csv file
            with open("gregg/expense-" + str(filing) + ".csv", "w", newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(list_of_rows)
        except:
            print("There might not be a anything here for file " + str(filing) + ".")
            continue
        print("Finished file number %s." % filing)
        time.sleep(3)
    print("Gregg's expenditures have been scraped.")


def get_gregg_contribs():

    # Loop through each of the filings for Gregg.
    for filing in gregg_filings:
        filing_page = contribs_base_url + str(filing)
        r = requests.get(filing_page)
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find('table', attrs={'class': 'frmDataGrid'})

        try:
    # Collect all of the rows from the table.
            list_of_rows = []
            for row in table.findAll('tr'):
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.strip().replace('\n', ' ')
                    list_of_cells.append(text)
                list_of_rows.append(list_of_cells)

    # Write the results to a csv file
            with open("gregg/contrib-" + str(filing) + ".csv", "w", newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(list_of_rows)
                print("Finished file number %s." % filing)
        except:
            print("There might not be a anything here for file " + str(filing) + ".")
            continue
        time.sleep(3)
    print("Gregg's contributions have been scraped.")


if __name__ == "__main__":
    # This function executes when you do "filingScraper.py" on the command line.
    print("Campaign finance snooping commencing...")
    main()
