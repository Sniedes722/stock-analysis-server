from distutils.core import setup
setup(
  name = 'stock-analysis-server',
  packages = ['live_stocks'],
  version = '0.1.0',
  description = 'Lightweight, real-time stock ticker server for building analysis algorithms & trading strategies in Python',
  author = 'Shawn Niederriter',
  url = 'https://github.com/Sniedes722/stock-analysis-server',
  keywords = ['googlefinance', 'stock', 'price' , 'finance', 'google', 'real-time', 'asyncio', 'async', 'requests'], # arbitrary keywords
  classifiers = [
    'License :: OSI Approved :: GNU General Public License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)