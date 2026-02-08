# Spliwise 

### Functional Requirements
- add users
- add expense
- view all transactions
- view in simplified format
- view balance (credit / debit) for each user
- settle balance

### Non Functional Requirements
- handle edge cases
- thread safe transactions


# LLD
### components
1. User -> details of user like name, id, balance
2. Transaction -> An event of transfer of money from one user to another 
3. Expense -> An event of payment by payer on behalf of set of users. Can be broken into transactions
4. Logbook -> maintains record of smallest unit ie. transaction
5. Splitwise -> core application interface binding all above components

### diagram
