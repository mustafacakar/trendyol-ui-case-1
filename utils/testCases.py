

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In main page, when user click butiques , he should see all images successfully'],
    ['Blocker', 'In Butique Page, user should see all images successfully'],
    ['Blocker', 'In Butique Page, when user click product, he should see Product detail Page'],
    ['Blocker', 'In Product Page, when user click Add To Basket, he should see Product in Basket']
]
