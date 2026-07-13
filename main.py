name: Build APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Set up Java (Android uchun shart)
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Install Android SDK & Accept Licenses
        uses: android-actions/setup-android@v3

      - name: Install Buildozer and dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libsqlite3-dev libgdbm-dev libssl-dev libbz2-dev libffi-dev build-essential
          pip install --user --upgrade buildozer cython virtualenv

      - name: Build with Buildozer
        run: |
          export PATH=$PATH:~/.local/bin
          buildozer init
          
          # Litsenziyalarni avtomat True qilish
          sed -i 's/.*android.accept_sdk_license.*/android.accept_sdk_license = True/' buildozer.spec
          
          # SDK yo'llarini GitHub-dagi tayyor SDK-ga yo'naltirish
          sed -i "s|# android.sdk_path =.*|android.sdk_path = $ANDROID_HOME|" buildozer.spec
          
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: bin/*.apk
