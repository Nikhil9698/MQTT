MQTT Android

Edit Build.gradle(APP)

dependencies {

    compile files('libs/org.eclipse.paho.android.service-1.1.1.jar')
    
    compile files('libs/org.eclipse.paho.client.mqttv3-1.1.1.jar')
    
}

Edit Build.gradle(Project)

repositories {

        google()
        
        jcenter()
        
        maven {
        
            url "https://repo.eclipse.org/content/repositories/paho-snapshots/"
            
        }
    }

Edit Mainfest

<uses-permission android:name="android.permission.INTERNET" />

<uses-permission android:name="android.permission.WAKE_LOCK" />

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<uses-permission android:name="android.permission.READ_PHONE_STATE" />


    
