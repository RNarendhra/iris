{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "iris Flower Classification.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IHqgWPoCj-or"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mbaHHma5NH4W",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "cabf6ccd-cc87-4071-db9b-6e937a96ab69"
      },
      "source": [
        "print(\" Hello this my first ML project\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " Hello this my first ML project\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZcEdhk0sj9Bv",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "884faf54-d387-4fbd-a3ba-1cca4e0fa1e2"
      },
      "source": [
        "print(\"Hello World\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello World\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Zrq7xk6vj-A_"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Zkh5-NXhkWrq",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCkgewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwogICAgICBwZXJjZW50LnRleHRDb250ZW50ID0KICAgICAgICAgIGAke01hdGgucm91bmQoKHBvc2l0aW9uIC8gZmlsZURhdGEuYnl0ZUxlbmd0aCkgKiAxMDApfSUgZG9uZWA7CiAgICB9CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "outputId": "2bf5c41b-f192-4bda-b212-4510be5fb567"
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from google.colab import files\n",
        "uploaded = files.upload()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-1aa6306e-1e02-4f1e-b9ac-e18938203a52\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-1aa6306e-1e02-4f1e-b9ac-e18938203a52\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "Saving iris.csv to iris.csv\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "neB89rfDKYCE"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RZikwishHdy3"
      },
      "source": [
        "import io\n",
        "iris = pd.read_csv(io.BytesIO(uploaded['iris.csv']))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sCWnG-g_IVoz",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 415
        },
        "outputId": "5f43d6f2-3e02-4068-9c3b-684f6360d2ac"
      },
      "source": [
        "iris"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "      <th>class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>iris_setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.3</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>6.3</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1.9</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.0</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>148</th>\n",
              "      <td>6.2</td>\n",
              "      <td>3.4</td>\n",
              "      <td>5.4</td>\n",
              "      <td>2.3</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>149</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.8</td>\n",
              "      <td>iris_virginica</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>150 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     sepal_length  sepal_width  petal_length   petal_width           class\n",
              "0             5.1          3.5           1.4           0.2     iris_setosa\n",
              "1             4.9          3.0           1.4           0.2     iris_setosa\n",
              "2             4.7          3.2           1.3           0.2     iris_setosa\n",
              "3             4.6          3.1           1.5           0.2     iris_setosa\n",
              "4             5.0          3.6           1.4           0.2     iris_setosa\n",
              "..            ...          ...           ...           ...             ...\n",
              "145           6.7          3.0           5.2           2.3  iris_virginica\n",
              "146           6.3          2.5           5.0           1.9  iris_virginica\n",
              "147           6.5          3.0           5.2           2.0  iris_virginica\n",
              "148           6.2          3.4           5.4           2.3  iris_virginica\n",
              "149           5.9          3.0           5.1           1.8  iris_virginica\n",
              "\n",
              "[150 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1MWAKoROKaJg",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "9a7c4e98-a6fc-4430-c780-0cc8bbb856ef"
      },
      "source": [
        "print(iris.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(150, 5)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "itAdU0hmLyZ2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 294
        },
        "outputId": "e6c23994-9c4d-45a6-f41f-c22cb38a129d"
      },
      "source": [
        "iris.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>150.000000</td>\n",
              "      <td>150.000000</td>\n",
              "      <td>150.000000</td>\n",
              "      <td>150.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5.843333</td>\n",
              "      <td>3.054000</td>\n",
              "      <td>3.758667</td>\n",
              "      <td>1.198667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.828066</td>\n",
              "      <td>0.433594</td>\n",
              "      <td>1.764420</td>\n",
              "      <td>0.763161</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>4.300000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>5.100000</td>\n",
              "      <td>2.800000</td>\n",
              "      <td>1.600000</td>\n",
              "      <td>0.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>5.800000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>4.350000</td>\n",
              "      <td>1.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>6.400000</td>\n",
              "      <td>3.300000</td>\n",
              "      <td>5.100000</td>\n",
              "      <td>1.800000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>7.900000</td>\n",
              "      <td>4.400000</td>\n",
              "      <td>6.900000</td>\n",
              "      <td>2.500000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       sepal_length  sepal_width  petal_length   petal_width\n",
              "count    150.000000   150.000000    150.000000    150.000000\n",
              "mean       5.843333     3.054000      3.758667      1.198667\n",
              "std        0.828066     0.433594      1.764420      0.763161\n",
              "min        4.300000     2.000000      1.000000      0.100000\n",
              "25%        5.100000     2.800000      1.600000      0.300000\n",
              "50%        5.800000     3.000000      4.350000      1.300000\n",
              "75%        6.400000     3.300000      5.100000      1.800000\n",
              "max        7.900000     4.400000      6.900000      2.500000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xN32E1cDMQg_",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 415
        },
        "outputId": "dc26eeb0-872b-432c-fd94-be30d68e66e4"
      },
      "source": [
        "x=iris.drop(columns=['class'])\n",
        "x\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>6.3</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1.9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>148</th>\n",
              "      <td>6.2</td>\n",
              "      <td>3.4</td>\n",
              "      <td>5.4</td>\n",
              "      <td>2.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>149</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.8</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>150 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     sepal_length  sepal_width  petal_length   petal_width\n",
              "0             5.1          3.5           1.4           0.2\n",
              "1             4.9          3.0           1.4           0.2\n",
              "2             4.7          3.2           1.3           0.2\n",
              "3             4.6          3.1           1.5           0.2\n",
              "4             5.0          3.6           1.4           0.2\n",
              "..            ...          ...           ...           ...\n",
              "145           6.7          3.0           5.2           2.3\n",
              "146           6.3          2.5           5.0           1.9\n",
              "147           6.5          3.0           5.2           2.0\n",
              "148           6.2          3.4           5.4           2.3\n",
              "149           5.9          3.0           5.1           1.8\n",
              "\n",
              "[150 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dPW0We9UQOsL",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "5fbe155c-55f3-4f2e-a688-d895128a5721"
      },
      "source": [
        "print(x.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(150, 4)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GZqaGjyXQWwB",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 225
        },
        "outputId": "038b3cd0-d6c1-43e6-8e8d-c8bd58001d95"
      },
      "source": [
        "y=iris['class']\n",
        "y"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0         iris_setosa\n",
              "1         iris_setosa\n",
              "2         iris_setosa\n",
              "3         iris_setosa\n",
              "4         iris_setosa\n",
              "            ...      \n",
              "145    iris_virginica\n",
              "146    iris_virginica\n",
              "147    iris_virginica\n",
              "148    iris_virginica\n",
              "149    iris_virginica\n",
              "Name: class, Length: 150, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OMX3w3XqO5bH"
      },
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.4)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oTdEPTPQNgwo"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "irv58frOQ5yb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 415
        },
        "outputId": "662a037a-f396-470f-cc4f-5034dbed8ab2"
      },
      "source": [
        "x_train"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>5.4</td>\n",
              "      <td>3.7</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>101</th>\n",
              "      <td>5.8</td>\n",
              "      <td>2.7</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>132</th>\n",
              "      <td>6.4</td>\n",
              "      <td>2.8</td>\n",
              "      <td>5.6</td>\n",
              "      <td>2.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>113</th>\n",
              "      <td>5.7</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>106</th>\n",
              "      <td>4.9</td>\n",
              "      <td>2.5</td>\n",
              "      <td>4.5</td>\n",
              "      <td>1.7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>110</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.2</td>\n",
              "      <td>5.1</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>62</th>\n",
              "      <td>6.0</td>\n",
              "      <td>2.2</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>85</th>\n",
              "      <td>6.0</td>\n",
              "      <td>3.4</td>\n",
              "      <td>4.5</td>\n",
              "      <td>1.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.6</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>120 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     sepal_length  sepal_width  petal_length   petal_width\n",
              "10            5.4          3.7           1.5           0.2\n",
              "101           5.8          2.7           5.1           1.9\n",
              "132           6.4          2.8           5.6           2.2\n",
              "113           5.7          2.5           5.0           2.0\n",
              "106           4.9          2.5           4.5           1.7\n",
              "..            ...          ...           ...           ...\n",
              "110           6.5          3.2           5.1           2.0\n",
              "62            6.0          2.2           4.0           1.0\n",
              "85            6.0          3.4           4.5           1.6\n",
              "0             5.1          3.5           1.4           0.2\n",
              "29            4.7          3.2           1.6           0.2\n",
              "\n",
              "[120 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RF-ge_2oQ-Gg",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 225
        },
        "outputId": "a9c35440-cfde-4882-d802-dab246cf203a"
      },
      "source": [
        "y_train"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10         iris_setosa\n",
              "101     iris_virginica\n",
              "132     iris_virginica\n",
              "113     iris_virginica\n",
              "106     iris_virginica\n",
              "            ...       \n",
              "110     iris_virginica\n",
              "62     iris_versicolor\n",
              "85     iris_versicolor\n",
              "0          iris_setosa\n",
              "29         iris_setosa\n",
              "Name: class, Length: 120, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TlOyihNAMHu1"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GTWutR6NRCrw",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 969
        },
        "outputId": "fde28ecf-2ea7-4e37-c440-01c9dbf776f7"
      },
      "source": [
        "x_test"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>120</th>\n",
              "      <td>6.9</td>\n",
              "      <td>3.2</td>\n",
              "      <td>5.7</td>\n",
              "      <td>2.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>5.8</td>\n",
              "      <td>4.0</td>\n",
              "      <td>1.2</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.6</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>121</th>\n",
              "      <td>5.6</td>\n",
              "      <td>2.8</td>\n",
              "      <td>4.9</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32</th>\n",
              "      <td>5.2</td>\n",
              "      <td>4.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>91</th>\n",
              "      <td>6.1</td>\n",
              "      <td>3.0</td>\n",
              "      <td>4.6</td>\n",
              "      <td>1.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>69</th>\n",
              "      <td>5.6</td>\n",
              "      <td>2.5</td>\n",
              "      <td>3.9</td>\n",
              "      <td>1.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>41</th>\n",
              "      <td>4.5</td>\n",
              "      <td>2.3</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>48</th>\n",
              "      <td>5.3</td>\n",
              "      <td>3.7</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>78</th>\n",
              "      <td>6.0</td>\n",
              "      <td>2.9</td>\n",
              "      <td>4.5</td>\n",
              "      <td>1.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>142</th>\n",
              "      <td>5.8</td>\n",
              "      <td>2.7</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>61</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>4.2</td>\n",
              "      <td>1.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>128</th>\n",
              "      <td>6.4</td>\n",
              "      <td>2.8</td>\n",
              "      <td>5.6</td>\n",
              "      <td>2.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>109</th>\n",
              "      <td>7.2</td>\n",
              "      <td>3.6</td>\n",
              "      <td>6.1</td>\n",
              "      <td>2.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>43</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.6</td>\n",
              "      <td>0.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>56</th>\n",
              "      <td>6.3</td>\n",
              "      <td>3.3</td>\n",
              "      <td>4.7</td>\n",
              "      <td>1.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>74</th>\n",
              "      <td>6.4</td>\n",
              "      <td>2.9</td>\n",
              "      <td>4.3</td>\n",
              "      <td>1.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>141</th>\n",
              "      <td>6.9</td>\n",
              "      <td>3.1</td>\n",
              "      <td>5.1</td>\n",
              "      <td>2.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>52</th>\n",
              "      <td>6.9</td>\n",
              "      <td>3.1</td>\n",
              "      <td>4.9</td>\n",
              "      <td>1.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>107</th>\n",
              "      <td>7.3</td>\n",
              "      <td>2.9</td>\n",
              "      <td>6.3</td>\n",
              "      <td>1.8</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>124</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.3</td>\n",
              "      <td>5.7</td>\n",
              "      <td>2.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>54</th>\n",
              "      <td>6.5</td>\n",
              "      <td>2.8</td>\n",
              "      <td>4.6</td>\n",
              "      <td>1.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.4</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>38</th>\n",
              "      <td>4.4</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>47</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>122</th>\n",
              "      <td>7.7</td>\n",
              "      <td>2.8</td>\n",
              "      <td>6.7</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.4</td>\n",
              "      <td>1.6</td>\n",
              "      <td>0.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>93</th>\n",
              "      <td>5.0</td>\n",
              "      <td>2.3</td>\n",
              "      <td>3.3</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>137</th>\n",
              "      <td>6.4</td>\n",
              "      <td>3.1</td>\n",
              "      <td>5.5</td>\n",
              "      <td>1.8</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     sepal_length  sepal_width  petal_length   petal_width\n",
              "120           6.9          3.2           5.7           2.3\n",
              "14            5.8          4.0           1.2           0.2\n",
              "25            5.0          3.0           1.6           0.2\n",
              "121           5.6          2.8           4.9           2.0\n",
              "32            5.2          4.1           1.5           0.1\n",
              "91            6.1          3.0           4.6           1.4\n",
              "69            5.6          2.5           3.9           1.1\n",
              "41            4.5          2.3           1.3           0.3\n",
              "48            5.3          3.7           1.5           0.2\n",
              "78            6.0          2.9           4.5           1.5\n",
              "142           5.8          2.7           5.1           1.9\n",
              "61            5.9          3.0           4.2           1.5\n",
              "128           6.4          2.8           5.6           2.1\n",
              "109           7.2          3.6           6.1           2.5\n",
              "43            5.0          3.5           1.6           0.6\n",
              "56            6.3          3.3           4.7           1.6\n",
              "74            6.4          2.9           4.3           1.3\n",
              "141           6.9          3.1           5.1           2.3\n",
              "52            6.9          3.1           4.9           1.5\n",
              "107           7.3          2.9           6.3           1.8\n",
              "124           6.7          3.3           5.7           2.1\n",
              "54            6.5          2.8           4.6           1.5\n",
              "6             4.6          3.4           1.4           0.3\n",
              "38            4.4          3.0           1.3           0.2\n",
              "47            4.6          3.2           1.4           0.2\n",
              "17            5.1          3.5           1.4           0.3\n",
              "122           7.7          2.8           6.7           2.0\n",
              "26            5.0          3.4           1.6           0.4\n",
              "93            5.0          2.3           3.3           1.0\n",
              "137           6.4          3.1           5.5           1.8"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ek7EJ6kwRIjh",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 555
        },
        "outputId": "c14c1bea-a51b-4c83-8446-b8e2c1e39225"
      },
      "source": [
        "y_test"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "120     iris_virginica\n",
              "14         iris_setosa\n",
              "25         iris_setosa\n",
              "121     iris_virginica\n",
              "32         iris_setosa\n",
              "91     iris_versicolor\n",
              "69     iris_versicolor\n",
              "41         iris_setosa\n",
              "48         iris_setosa\n",
              "78     iris_versicolor\n",
              "142     iris_virginica\n",
              "61     iris_versicolor\n",
              "128     iris_virginica\n",
              "109     iris_virginica\n",
              "43         iris_setosa\n",
              "56     iris_versicolor\n",
              "74     iris_versicolor\n",
              "141     iris_virginica\n",
              "52     iris_versicolor\n",
              "107     iris_virginica\n",
              "124     iris_virginica\n",
              "54     iris_versicolor\n",
              "6          iris_setosa\n",
              "38         iris_setosa\n",
              "47         iris_setosa\n",
              "17         iris_setosa\n",
              "122     iris_virginica\n",
              "26         iris_setosa\n",
              "93     iris_versicolor\n",
              "137     iris_virginica\n",
              "Name: class, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EdFsuN4jRXFQ"
      },
      "source": [
        "from sklearn import neighbors\n",
        "classifier1=neighbors.KNeighborsClassifier()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Azi5ANPvRY4v",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        },
        "outputId": "3679ab9f-5b2a-4a49-afd4-f561ddb722ec"
      },
      "source": [
        "classifier1.fit(x_train,y_train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
              "                     metric_params=None, n_jobs=None, n_neighbors=5, p=2,\n",
              "                     weights='uniform')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UO6u5MDnRjJ_"
      },
      "source": [
        "predictions=classifier1.predict(x_test)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZAPK9wfrRprS",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "429f75a8-1607-4cc3-8e82-ca416aa35096"
      },
      "source": [
        "from sklearn.metrics import accuracy_score\n",
        "print(accuracy_score(y_test,predictions))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.9333333333333333\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fQrwdhH1WSOT"
      },
      "source": [
        "from sklearn import tree\n",
        "classifier2=tree.DecisionTreeClassifier()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KfDxMj3mWahQ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "2a7a61d4-9597-4299-d6b5-18cc2243c6b9"
      },
      "source": [
        "classifier2.fit(x_train,y_train)\n",
        "predictions=classifier2.predict(x_test)\n",
        "from sklearn.metrics import accuracy_score\n",
        "print(accuracy_score(y_test,predictions))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.95\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}