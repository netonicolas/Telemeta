Telemeta 1.6 is finally out!
############################

:category: Releases

   * Minor bug fixes and improvments
   * Fix HTML5 audio compatibility (#173) for the web audio player. The SoundManager Flash player fallback should not be used in most modern web browser. Media files are now serves through Nginx (#155) which enables to stream music with byte range requests.
   * Add a User permission "can_run_analysis" to specify that a user or a group of users has the right to list and select advanced Timeside analysis to be displayed in the Timeside web audio player.
   * Temporarily remove Timeside server from INSTALLED_APPS until the development of this application is more advanced and is really used by Telemeta.
  
  
